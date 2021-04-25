# Generated by Django 2.2.4 on 2021-04-25 17:31

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0008_auto_20210425_1714'),
    ]

    operations = [
        migrations.CreateModel(
            name='Academic_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=200)),
                ('area_of_qualification', models.CharField(max_length=200)),
                ('category_of_university', models.CharField(max_length=200)),
                ('institute', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('Completed', 'Completed'), ('ResultAwaited', 'ResultAwaited'), ('FinalAwaited', 'FinalAwaited'), ('Ongoing', 'Ongoing')], max_length=200)),
                ('year_of_passing', models.IntegerField()),
                ('percentage', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publications', models.FileField(blank=True, null=True, upload_to='uploads/')),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('caste_certificate', models.FileField(blank=True, null=True, upload_to='uploads/')),
            ],
        ),
        migrations.CreateModel(
            name='Other_important_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('awards_and_recognition', models.TextField()),
                ('any_other_relevant_information', models.TextField()),
                ('reference', models.TextField()),
                ('statement_of_objective', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Professional_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organisation', models.CharField(max_length=200)),
                ('designation', models.CharField(max_length=200)),
                ('from_year', models.IntegerField()),
                ('to_year', models.IntegerField()),
                ('role', models.CharField(max_length=250)),
                ('pay_scale', models.IntegerField()),
                ('emoluments', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Teaching_and_research_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=200)),
                ('level', models.CharField(blank=True, choices=[('UG', 'Undergraduate'), ('PG', 'Postgraduate')], max_length=2, null=True)),
                ('sole_instructor', models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=1, null=True)),
                ('developer_of_course', models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No')], max_length=1, null=True)),
                ('name_of_student', models.CharField(max_length=200, null=True)),
                ('year_of_completion', models.IntegerField(blank=True, null=True)),
                ('name_of_institute', models.CharField(blank=True, max_length=200, null=True)),
                ('guide', models.CharField(blank=True, max_length=200, null=True)),
                ('organisation', models.CharField(blank=True, max_length=200, null=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('co_investigators', models.CharField(blank=True, max_length=200, null=True)),
                ('period', models.CharField(blank=True, max_length=100, null=True)),
                ('name_of_body', models.CharField(blank=True, max_length=150, null=True)),
                ('status_of_membership', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='applicant',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 4, 25, 17, 31, 12, 201814, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='General',
        ),
        migrations.AddField(
            model_name='teaching_and_research_detail',
            name='applicant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teaching_and_research_details', to='recruitment.Applicant'),
        ),
        migrations.AddField(
            model_name='professional_detail',
            name='applicant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='professional_details', to='recruitment.Applicant'),
        ),
        migrations.AddField(
            model_name='other_important_details',
            name='applicant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='other_details', to='recruitment.Applicant'),
        ),
        migrations.AddField(
            model_name='file',
            name='applicant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='recruitment.Applicant'),
        ),
        migrations.AddField(
            model_name='academic_detail',
            name='applicant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='academic_detail', to='recruitment.Applicant'),
        ),
    ]