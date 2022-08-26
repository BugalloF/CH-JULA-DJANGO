from django.shortcuts import render

# Create your views here.
from .models import Lessons, Person, School
from django.views import generic
def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_assignatures=Lessons.objects.all().count()

    num_users=Person.objects.all().count()  # El 'all()' esta implícito por defecto.

    
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={'num_assignatures':num_assignatures,'num_users':num_users},
    )

class PersonListView(generic.ListView):
    model = Person


def FriendshipsListView(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    person=Person.objects.all()


    
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'catalog/relationships_list.html',
        context={'person':person},
    )

class PersonDetailView(generic.DetailView):
    model = Person
    context_object_name = 'person'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PersonDetailView, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['lessons'] = School.objects.filter(person=self.kwargs['pk'])
        return context
