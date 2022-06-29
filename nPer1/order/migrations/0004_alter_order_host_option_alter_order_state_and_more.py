# Generated by Django 4.0.5 on 2022-06-29 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_store_foodcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='host_option',
            field=models.CharField(choices=[('button', 'button'), ('time', 'time'), ('count', 'count')], max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(choices=[('주문중', '주문중'), ('주문완료', '주문완료')], default='주문중', max_length=10),
        ),
        migrations.AlterField(
            model_name='store',
            name='foodCategory',
            field=models.CharField(choices=[('돈까스·회·일식', '돈까스·회·일식'), ('패스트푸드', '패스트푸드'), ('중식', '중식'), ('카페·디저트', '카페·디저트'), ('고기·구이', '고기·구이'), ('피자', '피자'), ('족발·보쌈', '족발·보쌈'), ('찜·찌개·탕', '찜·찌개·탕'), ('분식', '분식'), ('치킨', '치킨'), ('양식', '양식'), ('백반·죽·국수', '백반·죽·국수')], max_length=20),
        ),
    ]
