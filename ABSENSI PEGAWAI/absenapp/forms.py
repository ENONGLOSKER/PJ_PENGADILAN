from django import forms
from . models import absenModel,profil

# form untuk profil karyawan
class profilForm(forms.ModelForm):
    class Meta():
        model=profil #nama tabel
        fields="__all__" #ambil semu kolom
        
        # untuk merubah/ganti nama label 
        labels= {
            'jenisK' : 'Jenis Kelamin',
        }

        # untuk styling form
        widgets={
            'nama':forms.Select(
                attrs={
                    'class':'form-control',}
                ),
            'nip':forms.TextInput(
                attrs={
                    'class':'form-control',}
                ),
            'jenisK':forms.Select(
                attrs={
                    'class':'form-control',
                    'label':'Jenis Kelamin'}
                ),
            'jabatan':forms.TextInput(
                attrs={
                    'class':'form-control',}
                ),
            'alamat':forms.Textarea(
                attrs={
                    'class':'form-control',
                    'style':'height: 80px;',}
                ),
            }

# form untuk absen
class absenForm(forms.ModelForm):
    class Meta:
        model = absenModel
        fields = [
                # 'pegawai',
                'status',
                'ket',      
            ]
        widgets={
            # 'pegawai':forms.TextInput(
            #     attrs={
            #         'class':'form-control',}
            #     ),
            'status':forms.Select(
                attrs={
                    'class':'form-control',}
                ),
            'ket':forms.Textarea(
                attrs={
                    'class':'form-control',
                    'style':'height: 80px;',}
                ),
            }
