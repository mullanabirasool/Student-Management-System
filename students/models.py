from django.db import models


class Student(models.Model):

    id = models.AutoField(
        primary_key=True,
        db_column='ID'
    )

    date = models.DateField(
        db_column='DATE'
    )

    name = models.CharField(
        max_length=50,
        db_column='NAME'
    )

    mobile_no = models.CharField(
        max_length=15,
        db_column='MOBILE_NO'
    )

    alternate_no = models.CharField(
        max_length=20,
        db_column='ALTERNATE_NO',
        blank=True,
        null=True
    )

    email_id = models.CharField(
        max_length=50,
        db_column='EMAIL_ID',
        blank=True,
        null=True
    )

    address = models.TextField(
        db_column='ADDRESS',
        blank=True,
        null=True
    )

    course = models.CharField(
        max_length=50,
        db_column='COURSE'
    )

    batch = models.CharField(
        max_length=30,
        db_column='BATCH',
        blank=True,
        null=True
    )

    experience_fresher = models.CharField(
        max_length=30,
        db_column='EXPERIENCE_FRESHER',
        blank=True,
        null=True
    )

    how_you_know = models.CharField(
        max_length=50,
        db_column='HOW_YOU_KNOW',
        blank=True,
        null=True
    )

    contact = models.CharField(
        max_length=50,
        db_column='CONTACT',
        blank=True,
        null=True
    )

    counselor = models.CharField(
        max_length=50,
        db_column='COUNSELOR',
        blank=True,
        null=True
    )

    fees = models.IntegerField(
        default=0,
        db_column='FEES'
    )

    comment = models.TextField(
        db_column='COMMENT',
        blank=True,
        null=True
    )

    selected_type = models.CharField(
        max_length=30,
        db_column='SELECTED_TYPE',
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'student_details'
        managed = True

    def __str__(self):
        return self.name