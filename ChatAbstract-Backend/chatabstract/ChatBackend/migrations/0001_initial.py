# generated

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1000)),
                ('gpt', models.CharField(max_length=18000)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]