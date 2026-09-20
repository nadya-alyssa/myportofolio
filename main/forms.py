from django.forms import ModelForm, TextInput, Textarea, URLInput, Select, SelectDateWidget

from main.models import Experience, Education

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            "thumbnail",
            "started_at",
            "ended_at",
        ]

        labels = {
            "title": "Nama Pengalaman",
            "description": "Deskripsi Pengalaman",
            "category": "Kategori Pengalaman",
            "thumbnail": "URL Gambar Pengalaman",
            "started_at": "Tanggal Dimulai",
            "ended_at": "Tanggal Selesai",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Nama Pengalaman",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Pengalamanmu",
                    "rows": 3,
                }
            ),
            "category": Select(
                choices=Experience.EXPERIENCE_CHOICES,
                attrs={
                    "placeholder": "Pilih Kategori",
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
            "started_at": SelectDateWidget(
                years=range(1999, 2100),
            ),
            "ended_at": SelectDateWidget(
                years=range(1999, 2100),
            ),
        }

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = [
            "school",
            "level",
            "started_at",
            "ended_at",
        ]

        labels = {
            "school": "Nama Tempat Pendidikan",
            "level": "Jenjang Pendidikan",
            "started_at": "Tanggal Dimulai",
            "ended_at": "Tanggal Selesai",
        }

        widgets = {
            "school": TextInput(
                attrs={
                    "placeholder": "Nama Tempat Pendidikan",
                    "maxlength": 255,
                }
            ),
            "level": TextInput(
                attrs={
                    "placeholder": "Jenjang Pendidikan",
                    "maxlength": 255,
                }
            ),
            "started_at": SelectDateWidget(
                years=range(1999, 2100),
            ),
            "ended_at": SelectDateWidget(
                years=range(1999, 2100),
            ),
        }