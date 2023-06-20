# Generated by Django 2.1.15 on 2023-06-15 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_feedlyitem_id_alter_recipient_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewDisclosure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cve', models.CharField(max_length=20)),
                ('issue', models.CharField(max_length=200)),
                ('link', models.URLField()),
            ],
        ),
        migrations.AlterField(
            model_name='feedlyitem',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='recipient',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
