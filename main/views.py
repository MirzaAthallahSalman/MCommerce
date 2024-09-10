from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'MCommerce' : ' MCommerce',
        'nama_mahasiswa' : 'Mirza Athallah Salman',
        'kelas' : 'PBP A'
    }

    return render(request, "main.html", context)