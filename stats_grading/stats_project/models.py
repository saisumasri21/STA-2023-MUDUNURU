from django.db import models


class StudentDetails(models.Model):
    class Meta:
        db_table = 'student_details'
    First_Name = models.CharField(max_length=100, verbose_name='First Name')
    Last_name = models.CharField(max_length=100, verbose_name='Last Name')
    UID = models.CharField(max_length=12, primary_key=True, verbose_name='UID')
    Section_no = models.CharField(max_length=3, verbose_name='Sec-No')


class ProjectQuestions(models.Model):
    class Meta:
        db_table = 'project_questions'
    student_details = models.ForeignKey(StudentDetails, on_delete=models.CASCADE, blank=True, null=True, default='None')
    Exam_1_Score = models.FloatField(max_length=3, verbose_name='Exam-1 Score')
    Exam_2_Score = models.FloatField(max_length=3, verbose_name='Exam-2 Score')
    Q1 = models.FloatField(max_length=6, verbose_name='Q1: What is the sample size you have?')
    Q2 = models.FloatField(max_length=6, verbose_name='Q2: What is the 15% Trimmed mean of these 11 data points?')
    Q3 = models.FloatField(max_length=6, verbose_name='Q3: What is the sample mean of these 11 data points?')
    Q4 = models.FloatField(max_length=6, verbose_name='Q4: What is the sample standard deviation of these 11 '
                                                      'data points?')
    Q5 = models.FloatField(max_length=6, verbose_name='Q5: What is the sample variance of these 11 data points?')
    Q6 = models.FloatField(max_length=6, verbose_name='Q6: What is the sample range of these 11 data points?')
    Q7 = models.FloatField(max_length=6, verbose_name='Q7: What is the first(lower) Quartile of these 11 data points?')
    Q8 = models.FloatField(max_length=6, verbose_name='Q8: What is the second Quartile of these 11 data points?')
    Q9 = models.FloatField(max_length=6, verbose_name='Q9: What is the third(upper) Quartile of these 11 data points?')
    Q10 = models.FloatField(max_length=6, verbose_name='Q10: What is the Inter-Quartile Range?')
    Q11 = models.FloatField(max_length=15, verbose_name='Q11: What is the mode of these 11 data points?')
    Q12 = models.FloatField(max_length=6, verbose_name='Q12: What is the median of these 11 data points?')
    Q13_CHOICES = (
        ('SYMMETRIC', 'Symmetric'),
        ('LEFT SKEWED', 'Left Skewed'),
        ('RIGHT SKEWED', 'Right Skewed'),
        ('UNIFORM', 'Unifor'),
    )
    Q13 = models.CharField(max_length=15, choices=Q13_CHOICES, verbose_name='Q13: What is the rough shape of these data?'
                                                                           'Use comparison of mean and median to '
                                                                           'answer this')
    Q14 = models.FloatField(max_length=6, verbose_name='Q14: What is the probability that you choose an odd number or a'
                                                       'multiple of five from these data?')
    Q15 = models.FloatField(max_length=6, verbose_name='Q15: What is the probability of choosing an odd number '
                                                       'and a prime number from these data?')
    Q16 = models.FloatField(max_length=6, verbose_name='Q16: What is the probability that a randomly chosen number '
                                                       'among'
                                                       'these 11 data points is between 91 and 100, inclusive of '
                                                       'the end points?')
    Q17 = models.FloatField(max_length=6, verbose_name='Q17: What is the probability that a randomly chosen number '
                                                       'among'
                                                       'these 11 data points is between 95 and 100, exclusive of '
                                                       'the end points?')
    Q18 = models.FloatField(max_length=6, verbose_name='Q18: What is the probability that a randomly chosen number '
                                                       'among'
                                                       'these 11 data points is less than 90, (excluding 90)?')
    Q19 = models.FloatField(max_length=6, verbose_name='Q19: What is the probability that a randomly chosen number '
                                                       'among'
                                                       'these 11 data points is not a multiple of 5?')
    Q20 = models.FloatField(max_length=6, verbose_name='Q20: What is the probability that a randomly chosen number '
                                                       'among'
                                                       'these 11 data points is an even number given that it is '
                                                       'multiple of 4?')
    Q21 = models.FloatField(max_length=6, verbose_name='Q21: If we choose a student at random, what is the probability '
                                                       'that student received grade-D?')
    Q22 = models.FloatField(max_length=6, verbose_name='Q22: If C or above is considered as a pass grade, and '
                                                       'if we chose a sudent at random, what is the probability '
                                                       'that the student received a pass grade?')
    Q23 = models.FloatField(max_length=6, verbose_name='Q23: What is the probability that the student selected at '
                                                       'random got a fail grade?')
    Q24 = models.FloatField(max_length=15, verbose_name='Q24: What is the probability that a student selected at random '
                                                       'got a B or A grade?')
    Q25_CHOICES = (
        ('YES', 'Yes'),
        ('NO', 'white'),
        ('NOT SURE', 'Not sure'),
    )
    Q25 = models.CharField(max_length=6, choices=Q25_CHOICES, verbose_name='Q25: Is Q24 considered as mutually '
                                                                                  'exclusive case?')


class ProjectGrading(models.Model):
    class Meta:
        db_table = 'project_grading'
    student_details = models.ForeignKey(StudentDetails, on_delete=models.CASCADE, blank=True, null=True, default='None')
    Q_1 = models.IntegerField(default=0)
    Q_2 = models.IntegerField(default=0)
    Q_3 = models.IntegerField(default=0)
    Q_4 = models.IntegerField(default=0)
    Q_5 = models.IntegerField(default=0)
    Q_6 = models.IntegerField(default=0)
    Q_7 = models.IntegerField(default=0)
    Q_8 = models.IntegerField(default=0)
    Q_9 = models.IntegerField(default=0)
    Q_10 = models.IntegerField(default=0)
    Q_11 = models.IntegerField(default=0)
    Q_12 = models.IntegerField(default=0)
    Q_13 = models.IntegerField(default=0)
    Q_14 = models.IntegerField(default=0)
    Q_15 = models.IntegerField(default=0)
    Q_16 = models.IntegerField(default=0)
    Q_17 = models.IntegerField(default=0)
    Q_18 = models.IntegerField(default=0)
    Q_19 = models.IntegerField(default=0)
    Q_20 = models.IntegerField(default=0)
    Q_21 = models.IntegerField(default=0)
    Q_22 = models.IntegerField(default=0)
    Q_23 = models.IntegerField(default=0)
    Q_24 = models.IntegerField(default=0)
    Q_25 = models.IntegerField(default=0)
    project_score = models.IntegerField(default=0)

