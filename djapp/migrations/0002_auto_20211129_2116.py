# Generated by Django 3.2.7 on 2021-11-29 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinfo',
            options={'verbose_name': '图书'},
        ),
        migrations.AlterModelOptions(
            name='peopleinfo',
            options={'verbose_name': '人物信息'},
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='commentcount',
            field=models.IntegerField(default=0, verbose_name='评论量'),
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='逻辑删除'),
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='pub_date',
            field=models.DateField(null=True, verbose_name='发布日期'),
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='readcount',
            field=models.IntegerField(default=0, verbose_name='阅读量'),
        ),
        migrations.AddField(
            model_name='peopleinfo',
            name='description',
            field=models.CharField(max_length=200, null=True, verbose_name='描述信息'),
        ),
        migrations.AddField(
            model_name='peopleinfo',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='逻辑删除'),
        ),
        migrations.AlterField(
            model_name='bookinfo',
            name='name',
            field=models.CharField(max_length=20, verbose_name='名称'),
        ),
        migrations.AlterField(
            model_name='peopleinfo',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djapp.bookinfo', verbose_name='图书'),
        ),
        migrations.AlterField(
            model_name='peopleinfo',
            name='gender',
            field=models.SmallIntegerField(choices=[(0, 'male'), (1, 'female')], default=0, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='peopleinfo',
            name='name',
            field=models.CharField(max_length=20, verbose_name='名称'),
        ),
        migrations.AlterModelTable(
            name='bookinfo',
            table='bookinfo',
        ),
        migrations.AlterModelTable(
            name='peopleinfo',
            table='peopleinfo',
        ),
    ]
