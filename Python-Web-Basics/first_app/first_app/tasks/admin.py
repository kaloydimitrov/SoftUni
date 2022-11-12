
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]
