# Generated by Django 3.2.3 on 2021-06-06 16:01

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import recruitment.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('application_no', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('date', models.DateField(default=datetime.datetime(2021, 6, 6, 16, 1, 21, 350154, tzinfo=utc))),
                ('advertisement_no', models.TextField()),
                ('post', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=20)),
                ('Research_Domain', models.TextField(default=None)),
                ('profile_picture', models.FileField(blank=True, null=True, upload_to=recruitment.models.handle_uploaded_file)),
            ],
        ),
        migrations.CreateModel(
            name='ThesisSubmitted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PhD_title', models.CharField(max_length=200)),
                ('Research_Domain', models.CharField(max_length=200)),
                ('Institute_Name', models.CharField(max_length=200)),
                ('University_Name', models.CharField(max_length=200)),
                ('Registration_Date', models.CharField(max_length=200)),
                ('Submission_Date', models.CharField(max_length=200)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ThesisSubmitted', to='recruitment.applicant')),
            ],
        ),
        migrations.CreateModel(
            name='Thesis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ongoing_phd', models.TextField()),
                ('completed_phd', models.TextField()),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Thesis', to='recruitment.applicant')),
            ],
        ),
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('defence_date', models.DateField()),
                ('total_exp', models.CharField(max_length=10)),
                ('exp_post_phd', models.TextField()),
                ('total_phd_students', models.CharField(max_length=20)),
                ('ongoing_phd_supervision', models.TextField()),
                ('total_projects', models.CharField(max_length=10)),
                ('ongoing_projects', models.CharField(max_length=20)),
                ('computational_projects', models.TextField()),
                ('SCI_journal', models.TextField()),
                ('SCI_journal_post_phd', models.TextField()),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='summary', to='recruitment.applicant')),
            ],
        ),
        migrations.CreateModel(
            name='SponsoredProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spo_tot_number', models.CharField(max_length=10)),
                ('spo_ongoing', models.TextField()),
                ('spo_completed', models.TextField()),
                ('spo_file', models.FileField(blank=True, null=True, upload_to=recruitment.models.handle_uploaded)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sponsored_project', to='recruitment.applicant')),
            ],
        ),
        migrations.CreateModel(
            name='SeminarArticles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.TextField()),
                ('seminar_subject', models.TextField()),
                ('location', models.CharField(max_length=100)),
                ('From', models.CharField(max_length=20)),
                ('to', models.CharField(max_length=20)),
                ('published', models.TextField()),
                ('supporting_documents', models.ImageField(blank=True, null=True, upload_to=recruitment.models.handle_uploaded)),
                ('duration', models.CharField(max_length=20)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seminararticles', to='recruitment.applicant')),
            ],
        ),
        migrations.CreateModel(
            name='ResearchExp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('From', models.CharField(max_length=20)),
                ('to', models.CharField(max_length=20)),
                ('number_of_months', models.TextField()),
                ('supporting_documents', models.ImageField(blank=True, null=True, upload_to=recruitment.models.handle_uploaded)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='research_exp', to='recruitment.applicant')),
            ],
        ),
        migrations.CreateModel(
            name='PhDOngoing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PhD_title', models.CharField(max_length=200)),
                ('Research_Domain', models.CharField(max_length=200)),
                ('Institute_Name', models.CharField(max_length=200)),
                ('University_Name', models.CharField(max_length=200)),
                ('Registration_Date', models.CharField(max_length=200)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PhDOngoing', to='recruitment.applicant')),
            ],
        ),
        migrations.CreateModel(
            name='PhDAwarded',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PhD_title', models.CharField(max_length=200)),
                ('Research_Domain', models.CharField(max_length=200)),
                ('Institute_Name', models.CharField(max_length=200)),
                ('University_Name', models.CharField(max_length=200)),
                ('Registration_Date', models.CharField(max_length=200)),
                ('Defense_Date', models.CharField(max_length=200)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PhDAwarded', to='recruitment.applicant')),
            ],
        ),
        migrations.CreateModel(
            name='PhD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PhD_awarded', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('PhD_details', models.CharField(choices=[('Ongoing', 'Ongoing'), ('Submitted', 'Thesis Submitted'), ('Awarded', 'Awarded')], max_length=11)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PhD', to='recruitment.applicant')),
            ],
        ),
        migrations.CreateModel(
            name='Patent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patent_details', models.TextField()),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patent', to='recruitment.applicant')),
            ],
        ),
        migrations.CreateModel(
            name='OtherInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membership', models.TextField()),
                ('responsibilities', models.TextField()),
                ('Any_other_relevant_information', models.TextField()),
                ('academic_year_break', models.TextField()),
                ('college_punishment', models.TextField()),
                ('judicial_punishment', models.TextField()),
                ('unfit_for_position', models.TextField()),
                ('reference1', models.TextField()),
                ('reference2', models.TextField()),
                ('reference3', models.TextField()),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='other_info', to='recruitment.applicant')),
            ],
        ),
        migrations.CreateModel(
            name='NewspaperArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.TextField()),
                ('journal_name', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('date_published', models.CharField(max_length=20)),
                ('vol_no', models.TextField()),
                ('referred', models.TextField()),
                ('naas', models.TextField()),
                ('supporting_documents', models.ImageField(blank=True, null=True, upload_to=recruitment.models.handle_uploaded)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='newspaper_article', to='recruitment.applicant')),
            ],
        ),
        migrations.CreateModel(
            name='General',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('DOB', models.DateField()),
                ('father_name', models.CharField(max_length=200)),
                ('address_perm', models.CharField(max_length=200)),
                ('telephone_perm', models.CharField(max_length=20)),
                ('pin_perm', models.CharField(default=None, max_length=6)),
                ('address_mail', models.CharField(max_length=200)),
                ('telephone_mail', models.CharField(max_length=20)),
                ('pin_mail', models.CharField(default=None, max_length=6)),
                ('mobile_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=50)),
                ('gender', models.CharField(max_length=20)),
                ('marital_status', models.CharField(choices=[('Married', 'Married'), ('Not Married', 'Not Married')], max_length=11)),
                ('nationality', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('General', 'General'), ('OBC-CL', 'OBC-CL'), ('OBC-NCL', 'OBC-NCL'), ('ST', 'ST'), ('SC', 'SC'), ('Gen-PwD', 'Gen-PwD'), ('OBC-CL-PwD', 'OBC-CL-PwD'), ('OBC-NCL-PwD', 'OBC-NCL-PwD'), ('ST-PwD', 'ST-Pwd'), ('SC-PwD', 'SC-PwD')], max_length=11)),
                ('reservation', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
                ('reservation_certificate', models.ImageField(blank=True, null=True, upload_to=recruitment.models.handle_uploaded)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='General', to='recruitment.applicant')),
            ],
        ),
        migrations.CreateModel(
            name='Experiments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exp_tot_number', models.CharField(max_length=10)),
                ('exp_ongoing', models.TextField()),
                ('exp_completed', models.TextField()),
                ('exp_file', models.FileField(blank=True, null=True, upload_to=recruitment.models.handle_uploaded)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Experiments', to='recruitment.applicant')),
            ],
        ),
        migrations.CreateModel(
            name='EmploymentExp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('post', models.CharField(max_length=250)),
                ('from_year', models.CharField(max_length=20)),
                ('to_year', models.CharField(max_length=20)),
                ('salary', models.TextField()),
                ('nature', models.CharField(max_length=200)),
                ('supporting_documents', models.FileField(blank=True, null=True, upload_to=recruitment.models.handle_uploaded)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Employment_exp', to='recruitment.applicant')),
            ],
        ),
        migrations.CreateModel(
            name='EducationalQualifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('marks', models.CharField(max_length=10)),
                ('subjects', models.CharField(max_length=200)),
                ('year_of_passing', models.IntegerField()),
                ('supporting_documents', models.FileField(blank=True, null=True, upload_to=recruitment.models.handle_uploaded)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Educational_qualifications', to='recruitment.applicant')),
            ],
        ),
        migrations.CreateModel(
            name='Declaration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.TextField()),
                ('date', models.CharField(max_length=20)),
                ('signature', models.FileField(blank=True, null=True, upload_to=recruitment.models.handle_uploaded)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='declaration', to='recruitment.applicant')),
            ],
        ),
        migrations.CreateModel(
            name='Chapters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=100)),
                ('chapter', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=100)),
                ('date_of_publisher', models.CharField(max_length=20)),
                ('isbn_issn', models.TextField()),
                ('supporting_documents', models.ImageField(blank=True, null=True, upload_to=recruitment.models.handle_uploaded)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicant', to='recruitment.applicant')),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=100)),
                ('date_publish', models.CharField(max_length=20)),
                ('isbn', models.TextField()),
                ('supporting_documents', models.ImageField(blank=True, null=True, upload_to=recruitment.models.handle_uploaded)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='recruitment.applicant')),
            ],
        ),
        migrations.CreateModel(
            name='AdministrativeDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('administrative_details', models.TextField()),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='administrative_details', to='recruitment.applicant')),
            ],
        ),
    ]
