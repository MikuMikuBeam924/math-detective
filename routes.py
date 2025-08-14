from flask import render_template, request, session, redirect, url_for, jsonify
from app import app
import time
from game_data import EXERCISES, SUSPECTS, SAFE_CLUES, CULPRIT

@app.before_request
def init_session():
    if 'game_started' not in session:
        session['game_started'] = False
        session['start_time'] = None
        session['saved_answers'] = {}
        session['solved_exercises'] = []
        session['collected_clues'] = []
        session['opened_safes'] = []

@app.route('/')
def index():
    if not session.get('game_started'):
        session['game_started'] = True
        session['start_time'] = time.time()
    areas = {}
    for ex in EXERCISES:
        areas.setdefault(ex['topic'], []).append(ex)
    return render_template('index.html', areas=areas, solved=session.get('solved_exercises', []),
                           suspects=SUSPECTS, collected=session.get('collected_clues', []))

@app.route('/solve_exercise', methods=['POST'])
def solve_exercise():
    exercise_id = int(request.form.get('exercise_id'))
    answer = request.form.get('answer','').strip()
    saved = session.get('saved_answers', {})
    saved[str(exercise_id)] = answer
    session['saved_answers'] = saved
    attempts = session.get('attempts', {})
    attempts[str(exercise_id)] = attempts.get(str(exercise_id), 0) + 1
    session['attempts'] = attempts

    ex = next((e for e in EXERCISES if e['id']==exercise_id), None)
    if ex:
        try:
            if int(answer) == int(ex['answer']) and exercise_id not in session.get('solved_exercises', []):
                solved = session.get('solved_exercises', [])
                solved.append(exercise_id)
                session['solved_exercises'] = solved
                safe_num = ex.get('safe')
                safe_ex_ids = [e['id'] for e in EXERCISES if e.get('safe')==safe_num]
                if all(eid in session.get('solved_exercises', []) for eid in safe_ex_ids):
                    opened = session.get('opened_safes', [])
                    if safe_num not in opened:
                        opened.append(safe_num)
                        session['opened_safes'] = opened
                        clues = SAFE_CLUES.get(safe_num, [])
                        collected = session.get('collected_clues', [])
                        for c in clues:
                            if c not in collected:
                                collected.append(c)
                        session['collected_clues'] = collected
        except ValueError:
            pass
    return jsonify({'status':'saved','saved_answer': answer,
                    'opened_safes': session.get('opened_safes', []),
                    'collected_clues': session.get('collected_clues', [])})

@app.route('/finish')
def finish():
    end_time = time.time()
    start_time = session.get('start_time') or end_time
    duration = int(end_time - start_time)
    topic_stats = {}
    for ex in EXERCISES:
        t = ex['topic']
        topic_stats.setdefault(t, {'total':0,'solved':0,'attempts':0})
        topic_stats[t]['total'] += 1
        if ex['id'] in session.get('solved_exercises', []):
            topic_stats[t]['solved'] += 1
        topic_stats[t]['attempts'] += session.get('attempts', {}).get(str(ex['id']), 0)
    tips = []
    for t,stats in topic_stats.items():
        if stats['solved'] < max(1, stats['total']//2):
            tips.append(f"Practica más ejercicios de {t}.")
    result = {'duration_seconds': duration, 'topic_stats': topic_stats,
              'tips': tips, 'collected_clues': session.get('collected_clues', []),
              'accused': session.get('accused', None)}
    return render_template('complete.html', result=result, suspects=SUSPECTS, culprit=CULPRIT)

@app.route('/accuse', methods=['POST'])
def accuse():
    suspect_id = request.form.get('suspect_id')
    session['accused'] = suspect_id
    session['game_completed'] = True
    return redirect(url_for('finish'))

@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('index'))
