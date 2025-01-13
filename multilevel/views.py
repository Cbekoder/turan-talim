import json

from django.shortcuts import render, redirect
from django.views import View
from main.models import Language
from multilevel.models import Listening, Reading, Writing, Speaking, UserTest, Question, Option


class MultilevelListView(View):
    def get(self, request):
        context = {
            'user': request.user,
            'languages': Language.objects.all()
        }
        return render(request, 'multilevels.html', context)

    def post(self, request, direction):
        pass


class MultilevelDetailView(View):
    def get(self, request, pk):
        context = {
            'user': request.user,
            'language': Language.objects.get(id=pk)
        }
        return render(request, 'multilevel-detail.html', context)

    def post(self, request, direction):
        pass


class MultilevelTestListeningView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            user = request.user
            lang = Language.objects.get(id=pk)
            unfinished_listening = UserTest.objects.filter(
                user=user,
                language=lang,
                listening__isnull=False,
                done_listening=False).order_by(
                'created_at').last()

            if unfinished_listening and False:
                listening = Listening.objects.get(id=unfinished_listening.listening.id)
            else:
                listening = Listening.objects.filter(language=lang).order_by('?')[0]
                UserTest(user=user, language=lang, listening=listening).save()

            listening_data = []
            tests = listening.test_set.all().order_by('order')

            for test in tests:
                questions = test.question_set.all()
                question_data = []

                for question in questions:
                    options = question.option_set.all()
                    question_data.append({
                        'question': question,
                        'options': options
                    })
                listening_data.append({
                    "test": test,
                    "questions": question_data
                })

            context = {
                'user': request.user,
                'listening': listening,
                'sections': listening_data,
            }
            return render(request, 'multilevel-testing-listening.html', context)
        return redirect('signing')

    def post(self, request, pk):
        if request.user.is_authenticated:
            user = request.user
            lang = Language.objects.get(id=pk)
            # unfinished_test = UserTest.objects.filter(user=user, language=lang, done_listening=False).order_by(
            #     'created_at').last()
            # answers = request.POST.dict()
            # if unfinished_test:
            #     listening = Listening.objects.get(id=unfinished_test.listening.id)
            # else:
            #     return redirect('404')
            #
            # tests = listening.test_set.all().order_by('order')
            # user_result = 0
            # user_options = {}
            # for test in tests:
            #     questions = test.question_set.all()
            #     for question in questions:
            #         if question.has_options:
            #             user_options[f'q{question.id}'] = answers.get(f'q{question.id}') or None
            #             if f'q{question.id}' in answers and answers.get(f'q{question.id}') is not None and answers.get(
            #                     f'q{question.id}') != '':
            #                 print(answers.get(f'q{question.id}'))
            #                 if Option.objects.get(id=int(answers.get(f'q{question.id}'))).is_correct:
            #                     user_result += 1
            #         else:
            #             user_options[f'q{question.id}'] = answers.get(f'q{question.id}') or None
            #             if question.answer == answers.get(f'q{question.id}'):
            #                 user_result += 1
            #
            # unfinished_test.done_listening = True
            # unfinished_test.listening_result = user_result
            # unfinished_test.listening_user_options = user_options
            # unfinished_test.save()

            return redirect('multilevel-reading', pk=lang.id)
        return redirect('signing')


class MultilevelTestReadingView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            user = request.user
            lang = Language.objects.get(id=pk)
            finished_listening = UserTest.objects.filter(
                user=user,
                language=lang,
                done_listening=True).order_by('created_at').last()
            unfinished_reading = UserTest.objects.filter(
                user=user,
                language=lang,
                done_reading=False).order_by('created_at').last()

            if finished_listening and False:
                reading = Reading.objects.get(id=finished_listening.listening.id)
            else:
                reading = Reading.objects.filter(language=lang).order_by('?')[0]
                UserTest(user=user, language=lang, reading=reading).save()

            reading_data = []
            tests = reading.test_set.all().order_by('order')

            for test in tests:
                questions = test.question_set.all()
                question_data = []

                for question in questions:
                    options = question.option_set.all()
                    question_data.append({
                        'question': question,
                        'options': options
                    })
                reading_data.append({
                    "test": test,
                    "questions": question_data
                })

            context = {
                'user': request.user,
                'reading': reading,
                'sections': reading_data,
            }
            return render(request, 'multilevel-testing-reading.html', context)
        return redirect('signing')

    def post(self, request, pk):
        if request.user.is_authenticated:
            user = request.user
            lang = Language.objects.get(id=pk)
            # unfinished_test = UserTest.objects.filter(user=user, language=lang, done_listening=False).order_by(
            #     'created_at').last()
            # answers = request.POST.dict()
            # if unfinished_test:
            # else:
            #     return redirect('404')
            #
            # listening = Listening.objects.get(id=unfinished_test.listening.id)
            # tests = listening.test_set.all().order_by('order')
            # user_result = 0
            # user_options = {}
            # for test in tests:
            #     questions = test.question_set.all()
            #     for question in questions:
            #         if question.has_options:
            #             user_options[f'q{question.id}'] = answers.get(f'q{question.id}') or None
            #             if f'q{question.id}' in answers and answers.get(f'q{question.id}') is not None and answers.get(
            #                     f'q{question.id}') != '':
            #                 if Option.objects.get(id=int(answers.get(f'q{question.id}'))).is_correct:
            #                     user_result += 1
            #         else:
            #             user_options[f'q{question.id}'] = answers.get(f'q{question.id}') or None
            #             if question.answer == answers.get(f'q{question.id}'):
            #                 user_result += 1
            # #
            # unfinished_test.done_listening = True
            # unfinished_test.listening_result = user_result
            # unfinished_test.listening_user_options = user_options
            # unfinished_test.save()
            #
            # with open('test.json', "w") as f:
            #     f.write(json.dumps(user_options))

            return redirect('multilevel-writing', pk=lang.id)
        return redirect('signing')


class MultilevelTestWritingView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            user = request.user
            lang = Language.objects.get(id=pk)
            finished_listening = UserTest.objects.filter(
                user=user,
                language=lang,
                done_listening=True).order_by('created_at').last()
            finished_reading = UserTest.objects.filter(
                user=user,
                language=lang,
                done_reading=False).order_by('created_at').last()
            unfinished_writing = UserTest.objects.filter(
                user=user,
                language=lang,
                done_writing=False).order_by('created_at').last()

            if finished_listening and False:
                writing = Reading.objects.get(id=finished_listening.listening.id)
            else:
                writing = Writing.objects.filter(language=lang).order_by('?')[0]
                UserTest(user=user, language=lang, writing=writing).save()


            context = {
                'user': request.user,
                'writing': writing
            }
            return render(request, 'multilevel-testing-writing.html', context)
        return redirect('signing')

    def post(self, request, pk):
        if request.user.is_authenticated:
            # user = request.user
            # lang = Language.objects.get(id=pk)
            # unfinished_test = UserTest.objects.filter(user=user, language=lang, done_listening=False).order_by(
            #     'created_at').last()
            # answers = request.POST.dict()
            # if unfinished_test:
            #     listening = Listening.objects.get(id=unfinished_test.listening.id)
            # else:
            #     return redirect('404')

            # tests = listening.test_set.all().order_by('order')
            # user_result = 0
            # user_options = {}


            # unfinished_test.done_listening = True
            # unfinished_test.listening_result = user_result
            # unfinished_test.listening_user_options = user_options
            # unfinished_test.save()

            # with open('test.json', "w") as f:
            #     f.write(json.dumps(user_options))

            return redirect("/")
        return redirect('signing')
