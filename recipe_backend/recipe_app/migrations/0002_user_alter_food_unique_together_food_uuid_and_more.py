# Generated by Django 4.0.1 on 2022-01-16 07:03

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('UUID', models.UUIDField(default=uuid.UUID('ed88256a-bf40-45b3-8833-381eb561a630'), primary_key=True, serialize=False)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='food',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='food',
            name='UUID',
            field=models.ForeignKey(default=uuid.UUID('18a7886f-4907-41b8-aac6-58b4335e55e0'), on_delete=django.db.models.deletion.CASCADE, to='recipe_app.user'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='UUID',
            field=models.ForeignKey(default=uuid.UUID('38043e37-084e-4b82-916b-33f288dc6534'), on_delete=django.db.models.deletion.CASCADE, to='recipe_app.user'),
        ),
        migrations.AlterUniqueTogether(
            name='food',
            unique_together={('UUID', 'name', 'datePurchased')},
        ),
        migrations.AlterUniqueTogether(
            name='recipe',
            unique_together={('id', 'UUID')},
        ),
        migrations.CreateModel(
            name='ShoppingListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=20)),
                ('daysBeforeExpire', models.IntegerField()),
                ('UUID', models.ForeignKey(default=uuid.UUID('eccf4843-9aba-4f5d-b8d9-e31158d1bbfb'), on_delete=django.db.models.deletion.CASCADE, to='recipe_app.user')),
            ],
            options={
                'unique_together': {('name', 'UUID')},
            },
        ),
    ]
