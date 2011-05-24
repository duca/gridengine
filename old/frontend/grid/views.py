# Create your views here.

from django.template import Context, loader
from django.http import HttpResponse

#aqui esta definido o que, do meu BD, e importado
from frontend.grid.models import NodeStat

def index(request):
    
    nodestatus = NodeStat.objects.all()
    t = loader.get_template('index.html')
    c = Context({
        'Grid_Load': nodestatus,
        })
    return HttpResponse(t.render(c))
