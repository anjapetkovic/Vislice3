import bottle
import model

SKRIVNOST = "DanesJeLepDan"
DATOTEKA_S_STANJEM = "stanje.json"
DATOTEKA_Z_BESEDAMI = "besede.txt"

vislice = model.Vislice(DATOTEKA_S_STANJEM, DATOTEKA_Z_BESEDAMI)
vislice.nalozi_igre_iz_datoteke()


@bottle.get("/")
def osnovna_stran():
    return bottle.template('index.tpl')

@bottle.post("/nova_igra/")
def nova_igra():
    id_igre = vislice.nova_igra()
    bottle.response.set_cookie('idigre', id_igre, secret=SKRIVNOST, path='/')
    bottle.redirect("/igra/")

@bottle.get("/igra/")
def pokazi_igro():
    id_igre = bottle.request.get_cookie('idigre', secret=SKRIVNOST)
    (igra, stanje) = vislice.igre[id_igre]
    return bottle.template("igra.tpl",
                           id_igre=id_igre,
                           igra=igra,
                           poskus=stanje)

@bottle.post("/igra/")
def ugibaj():
    id_igre = bottle.request.get_cookie('idigre', secret=SKRIVNOST)
    crka = bottle.request.forms.getunicode("crka")
    vislice.ugibaj(id_igre, crka)
    bottle.redirect("/igra/")


@bottle.get('/img/<picture>')
def serve_pictures(picture):
    return bottle.static_file(picture, root='img')


bottle.run(reloader=True, debug=True)

# "files.associations": {
#         "*.tpl": "html",..
#     },