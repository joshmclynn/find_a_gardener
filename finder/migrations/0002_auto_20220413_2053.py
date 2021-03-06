# Generated by Django 3.2 on 2022-04-13 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='needs',
            field=models.CharField(blank=True, choices=[('garden-maintenance', 'Garden-Maintenance'), ('garden-design', 'Garden-Design'), ('landscaping', 'Landscaping'), ('tree-surgery', 'Tree-Surgery')], max_length=255),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(blank=True, choices=[('customer', 'Customer'), ('business', 'Business')], max_length=255),
        ),
    ]
