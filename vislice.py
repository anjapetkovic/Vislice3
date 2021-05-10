import bottle
import model

vislice = model.Vislice()


@bottle.get("/")
def osnovna_stran():
    return bottle.template('index.tpl')

@bottle.get("/igra/")
def nova_igra():
    id_igre = vislice.nova_igra()
    bottle.redirect(f"/igra/{id_igre}/")

@bottle.get("/igra/<id_igre:int>/")
def pokazi_igro(id_igre):
    (igra, stanje) = vislice.igre[id_igre]
    return bottle.template("igra.tpl",
                           id_igre = id_igre,
                           igra=igra,
                           poskus=stanje)

@bottle.post("/igra/<id_igre:int>/")
def ugibaj(id_igre):
    crka = bottle.request.forms.getunicode("crka")
    vislice.ugibaj(id_igre, crka)
    bottle.redirect(f"/igra/{id_igre}/")


@bottle.get('/img/<picture>')
def serve_pictures(picture):
    return bottle.static_file(picture, root='img')

bottle.run(reloader=True, debug=True)

# "files.associations": {
#         "*.tpl": "html",..
#     },