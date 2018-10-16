from django.shortcuts import render
from .models import ProjectGrading, ProjectQuestions
from .form import StudentDetailsForm, ProjectQuestionsForm
import statistics
from decimal import Decimal
from django.http import HttpResponse


def student_details(request):
    if request.method == 'POST':
        form = StudentDetailsForm(request.POST)
        if form.is_valid():
             user = form.save(commit=False)
             user.save()
             return render(request, 'project_questions.html', {'form': form})
    else:
        form = StudentDetailsForm()
    return render(request, 'student_details.html', {'form': form})


def project_questions(request):
    if request.method == 'POST':
        form = ProjectQuestionsForm(request.POST)
        if form.is_valid():
             answers = form.save(commit=False)
             answers.user = request.user
             answers.save()
             student_answers = ProjectQuestions.objects.get(student_details=answers.student_details)
             a = [105, 91, 52, 86, 100, 96, 98, 109, 96]
             b1 = student_answers.Exam_1_Score
             c1 = student_answers.Exam_2_Score
             a.append(b1)
             a.append(c1)
             'Q1'
             Q1 = student_answers.Q1
             SamplesizeQ = len(a)
             print(SamplesizeQ)
             SamplesizeA = Q1
             grading = ProjectGrading.objects.create(student_details=answers.student_details)
             if SamplesizeA != SamplesizeQ:
                 grading.Q_1 = 0
             else:
                 grading.Q_1 = 4
             'Q2'
             b = sorted(a)
             f = 15
             Trimmeddata = float(((f / 100)) * SamplesizeQ)
             Trimmeddata1 = int(round(Trimmeddata, 0))
             p = 2 * Trimmeddata1
             i = 0
             j = -1
             while b[i] != b[j]:
                 del b[i]
                 del b[j]
                 print(b)
                 Samplesizeb = len(b)
                 if Samplesizeb == SamplesizeQ - p:
                     break
                 else:
                     i = 0
                     j = -1
             print(b)
             print(Trimmeddata1)
             TrimmedmeanQ = statistics.mean(b)
             TrimmedmeanQ1 = round(TrimmedmeanQ, 2)
             print(TrimmedmeanQ1)
             Trimmedmean = student_answers.Q2
             TrimmedmeanA = float(Trimmedmean)
             TrimmedmeanA1 = round(TrimmedmeanA, 2)
             if TrimmedmeanA1 != TrimmedmeanQ1:
                 grading.Q_2 = 0
             else:
                 grading.Q_2 = 4
             'Q3'
             SamplemeanQ = statistics.mean(a)
             SamplemeanQ1 = round(SamplemeanQ, 2)
             SamplemeanA = student_answers.Q3
             SamplemeanA1 = float(SamplemeanA)
             SamplemeanA2 = round(SamplemeanA1, 2)
             if SamplemeanA2 == SamplemeanQ1:
                 grading.Q_3 = 4
             else:
                 grading.Q_3 = 4
             'Q4'
             Samplestddev = statistics.stdev(a)
             SamplestddevQ = float(round(Samplestddev, 2))
             SamplestddevA = student_answers.Q4
             SamplestddevA1 = float(SamplemeanA)
             SamplestddevA2 = round(SamplemeanA1, 2)
             if SamplestddevA2 == SamplestddevQ:
                 grading.Q_4 = 4
             else:
                 grading.Q_4 = 0
             'Q5'
             Samplevar = statistics.variance(a)
             SamplevarQ = float(round(Samplevar, 2))
             SamplevarA = student_answers.Q5
             SamplevarA1 = float(SamplemeanA)
             SamplevarA2 = round(SamplemeanA1, 2)
             if SamplevarA2 == SamplevarQ:
                 grading.Q_5 = 4
             else:
                 grading.Q_5 = 0
             'Q6'
             s = sorted(a)
             Samplerange = s[-1] - s[0]
             SamplevarA = student_answers.Q6
             SamplevarA1 = float(SamplemeanA)
             SamplevarA2 = round(SamplemeanA1, 0)
             if SamplevarA2 == Samplevar:
                 grading.Q_6 = 4
             else:
                grading.Q_6 = 0
             'Q7'
             FirstQuartile = statistics.median_low(a)
             FirstQuartileA = student_answers.Q7
             FirstQuartileA1 = int(FirstQuartileA)
             if FirstQuartileA1 == FirstQuartile:
                 grading.Q_7 = 4
             else:
                 grading.Q_7 = 0
             'Q8'
             SecondQuartile = statistics.median(a)
             SecondQuartileQ = float(round(SecondQuartile, 2))
             SecondQuartileA = student_answers.Q8
             SecondQuartileA1 = float(SamplemeanA)
             SecondQuartileA2 = round(SamplemeanA1, 2)
             if SecondQuartileA2 == SecondQuartileQ:
                 grading.Q_8 = 4
             else:
                 grading.Q_8 = 0
             'Q9'
             ThirdQuartile = statistics.median_high(a)
             ThirdQuartileA = student_answers.Q9
             ThirdQuartileA1 = int(ThirdQuartileA)
             if ThirdQuartileA1 == ThirdQuartile:
                 grading.Q_9 = 4
             else:
                 grading.Q_9 = 0
             'Q10'
             Interquartilerange = ThirdQuartile - FirstQuartile
             InterquartilerangeA = student_answers.Q10
             InterquartilerangeA1 = int(InterquartilerangeA)
             if InterquartilerangeA1 == Interquartilerange:
                 grading.Q_10 = 4
             else:
                 grading.Q_10 = 0
             'Q12'
             Median = statistics.median(a)
             MedianQ = float(round(Median, 2))
             MedianA = student_answers.Q12
             MedianA1 = float(SamplemeanA)
             MedianA2 = round(SamplemeanA1, 2)
             if MedianA1 == MedianQ:
                 grading.Q_12 = 4
             else:
                 grading.Q_12 = 0
             'Q13'
             Shape_of_the_distribution = ''
             if SamplemeanQ1 == MedianQ:
                 Shape_of_the_distribution = 'Symmetric'
             if SamplemeanQ1 > MedianQ:
                 Shape_of_the_distribution = 'Right Skewed'
             if SamplemeanQ1 < MedianQ:
                 Shape_of_the_distribution = 'Left Skewed'
             Shape_of_the_distribution_A = student_answers.Q13
             if Shape_of_the_distribution_A == Shape_of_the_distribution:
                 grading.Q_13 = 4
             else:
                 grading.Q_13 = 0
             """m = sorted(a)
             n = len(m)
             odd = []
             prime = []
             p = 2
             for i in m:
                 if (i % 2) != 0:
                     odd.append(i)
                 for i in odd:
                     while p < i:
                         if (i % p) != 0:
                             prime.append(i)
                             break
                     p += 1
             n_odd = len(odd)
             n_prime = len(prime)
             setodd = set(odd)
             setprime = set(prime)
             setP = set.intersection(setodd, setprime)
             Intersection = list(setP)
             n_Intersecion = len(Intersection)
             'Q14'
             # Let d = list of multiples of five from a
             d = []
             n_multiples = len(d)
             setd = set(d)
             setM = set.intersection(setodd, setd)
             IntersectionM = list(setM)
             n_IntersectionM = len(IntersectionM)
             for i in a:
                 if (i % 5) == 0:
                     d.append(i)
             prob_OM = round(((n_odd / n) + (n_multiples / n) + (n_IntersectionM / n)), 2)
             prob_OMA = student_answers.Q14
             prob_OMA1 = float(prob_OMA)
             prob_OMA2 = round(prob_OMA1, 2)
             if prob_OMA2 == prob_OM:
                 grading.Q_14 = 4
             else:
                 grading.Q_14 = 0
             'Q15'
             'Probability of odd numbers and prime number in a '
             prob_OP = (n_Intersecion / n)
             prob_OPF = round(prob_OP, 2)
             prob_OPA = student_answers.Q15
             prob_OPA1 = float(prob_OPA)
             prob_OPA2 = round(prob_OPA1, 2)
             if prob_OPA2 == prob_OPF:
                 grading.Q_15 = 4
             else:
                 grading.Q_15 = 0"""
             'Q16 - Q20'
             subset_data16 = []
             subset_data17 = []
             subset_data18 = []
             subset_data19 = []
             subset_data20 = []
             t = sorted(a)
             for i in t:
                 if i >= 91 and i <= 100:
                     subset_data16.append(i)
                 if i > 95 and i < 100:
                     subset_data17.append(i)
                 if i < 90:
                     subset_data18.append(i)
                 if (i % 5) != 0:
                     subset_data19.append(i)
                 if (i % 2) == 0 and (i % 4) == 0:
                     subset_data20.append(i)
             'Q16'
             prob_16 = round((len(subset_data16) / len(t)), 2)
             prob_16A = student_answers.Q16
             prob_16A1 = float(prob_16A)
             prob_16A2 = round(prob_16A1, 2)
             if prob_16A2 == prob_16:
                 grading.Q_16 = 4
             else:
                 grading.Q_16 = 0
             'Q17'
             prob_17 = round((len(subset_data17) / len(t)), 2)
             prob_17A = student_answers.Q17
             prob_17A1 = float(prob_17A)
             prob_17A2 = round(prob_17A1, 2)
             if prob_17A2 == prob_17:
                 grading.Q_17 = 4
             else:
                 grading.Q_17 = 0
             'Q18'
             prob_18 = round((len(subset_data18) / len(t)), 2)
             prob_18A = student_answers.Q18
             prob_18A1 = float(prob_18A)
             prob_18A2 = round(prob_18A1, 2)
             if prob_18A2 == prob_18:
                 grading.Q_18 = 4
             else:
                 grading.Q_18 = 0
             'Q19'
             prob_19 = round((len(subset_data19) / len(t)), 2)
             prob_19A = student_answers.Q19
             prob_19A1 = float(prob_19A)
             prob_19A2 = round(prob_19A1, 2)
             if prob_19A2 == prob_19:
                 grading.Q_19 = 4
             else:
                 grading.Q_19 = 0
             'Q20'
             prob_20 = round((len(subset_data19) / len(t)), 2)
             prob_20A = student_answers.Q20
             prob_20A1 = float(prob_20A)
             prob_20A2 = round(prob_20A1, 2)
             if prob_20A2 == prob_20:
                 grading.Q_20 = 4
             else:
                 grading.Q_20 = 0
             'Q21 - Q25'
             Grade_dict = {'A': 7, 'B': 1, 'C': 0, 'D': 0, 'F': 1}
             if b1 >= 90:
                 Grade_dict['A'] += 1
             if 80 <= b1 < 90:
                 Grade_dict['B'] += 1
             if 70 <= b1 < 80:
                 Grade_dict['C'] += 1
             if 60 <= b1 < 70:
                 Grade_dict['D'] += 1
             if b1 < 60:
                 Grade_dict['F'] += 1
             if c1 >= 90:
                 Grade_dict['A'] += 1
             if 80 <= c1 < 90:
                 Grade_dict['B'] += 1
             if 70 <= c1 < 80:
                 Grade_dict['C'] += 1
             if 60 <= c1 < 70:
                 Grade_dict['D'] += 1
             if c1 < 60:
                 Grade_dict['F'] += 1
             list_of_grades = list(Grade_dict.values())
             sum_of_grades = sum(Decimal(i) for i in list_of_grades)
             print(sum_of_grades)
             set_of_grades = set(list_of_grades)
             'Q21'
             prob_21 = round((Grade_dict['D'] / sum_of_grades), 2)
             prob_21A = student_answers.Q21
             prob_21A1 = float(prob_21A)
             prob_21A2 = round(prob_21A1, 2)
             if prob_21A2 == prob_21:
                 grading.Q_21 = 4
             else:
                 grading.Q_21 = 0
             'Q22'
             pass_grades = ['A', 'B', 'C']
             list_of_pass_grades = []
             for key in pass_grades:
                 list_of_pass_grades.append(Grade_dict.get(key))
             print(list_of_pass_grades)
             prob_22 = round((sum(list_of_pass_grades) / sum_of_grades), 2)
             prob_22A = student_answers.Q22
             prob_22A1 = float(prob_22A)
             prob_22A2 = round(prob_22A1, 2)
             if prob_22A2 == prob_22:
                 grading.Q_22 = 4
             else:
                 grading.Q_22 = 0
             'Q23'
             fail_grades = ['D', 'F']
             list_of_fail_grades = []
             for key in fail_grades:
                 list_of_fail_grades.append(Grade_dict.get(key))
             prob_23 = round((sum(list_of_fail_grades) / sum_of_grades), 2)
             prob_23A = student_answers.Q23
             prob_23A1 = float(prob_23A)
             prob_23A2 = round(prob_23A1, 2)
             if prob_23A2 == prob_23:
                 grading.Q_23 = 4
             else:
                 grading.Q_23 = 0
             'Q24'
             prob_24 = round(((Grade_dict['A'] + Grade_dict['B']) / sum_of_grades))
             prob_24A = student_answers.Q24
             prob_24A1 = float(prob_24A)
             prob_24A2 = round(prob_24A1, 2)
             if prob_24A2 == prob_24:
                 grading.Q_24 = 4
             else:
                 grading.Q_24 = 0
             'Q25'
             Mutually_exclusive = 'Yes'
             Mutually_exclusiveA = student_answers.Q25
             if Mutually_exclusive == Mutually_exclusiveA:
                 grading.Q_25 = 4
             else:
                 grading.Q_25 = 0
             grading.save()
             return HttpResponse('Thank you your project responses have been saved. Have a nice day!')
    else:
        form = ProjectQuestionsForm()
    return render(request, 'project_questions.html', {'form': form})
