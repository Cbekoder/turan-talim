import json
import random
from django.shortcuts import render, redirect
from django.views import View

from core.utils import send_request
from exams.models import Exam, Question, Option, QuizLog

class ExamListView(View):
    def get(self, request, direction):
        exams = Exam.objects.filter(direction=direction)
        context = {
            'user': request.user,
            'exams': exams
        }
        return render(request, 'exams.html', context)

    def post(self, request, direction):
        pass


class ExamDetailView(View):
    def get(self, request, exam_id):
        exam = Exam.objects.get(id=exam_id)
        context = {
            'user': request.user,
            'exam': exam
        }
        return render(request, 'detail.html', context)

    def post(self, request, direction):
        pass


class ExamTestView(View):
    def get(self, request, exam_id):
        data = dict()
        data['page_title'] = 'Test'
        exam = Exam.objects.get(id=exam_id)
        data['exam'] = exam
        questions = Question.objects.filter(exam=exam.id)
        question_res = {}
        count = 1
        json_data = []
        for question in questions:
            options = list(Option.objects.filter(question_id=question.id))
            random.shuffle(options)
            json_datum = {
                "question": question.id,
            }
            option_order = [i.id for i in options]
            json_datum["options"] = option_order
            json_data.append(json_datum)
            question_res[count] = {
                "question": question,
                "options": options,
            }
            count += 1
        data['questions'] = question_res
        # print(data)
        jsondata = QuizLog.objects.create(json=json_data)
        data['log_id'] = jsondata.id
        return render(request, 'exam-testing.html', context=data)

    def post(self, request, exam_id):
        exam = Exam.objects.get(id=exam_id)
        questions = Question.objects.filter(exam=exam)
        result_data = {}

        for question in questions:
            selected_option_id = request.POST.get(f'q{question.id}')
            options = Option.objects.filter(question=question)
            question_data = {
                'question': question.text,
                'options': [],
            }

            for option in options:
                option_data = {
                    'id': option.id,
                    'text': option.text,
                    'is_correct': option.is_correct,
                    'is_selected': str(option.id) == selected_option_id,
                }
                question_data['options'].append(option_data)

            result_data[question.id] = question_data

        analysis = send_request(json.dumps(result_data))

        return render(request, 'exam-result.html', {
            'exam': exam,
            'result_data': result_data,
            'analysis': analysis
        })