% import model
% rebase('base.tpl', title='Igra')

<table>
    <tr>
        <td>{{igra.pravilni_del_gesla()}}</td>
    </tr>
    <tr>
        <td>Nepravilne črke: </td>
        <td>{{igra.nepravilni_ugibi()}} </td>
   </tr>
   <tr>
       <td><img src="/img/{{igra.stevilo_napak()}}.jpg" alt="obesanje"></td>
   </tr>
</table>

% if poskus == model.ZMAGA :

<h1>Zmaga!</h1>

Uganili ste pravilno geslo. Čestitke!

<form action="/nova_igra/" method="post">
    <button type="submit">Nova igra</button>
</form>

% elif poskus == model.PORAZ :

<h2>Izgubili ste!</h2>

Pravilno geslo je: {{igra.geslo}}

<form action="/nova_igra/" method="post">
    <button type="submit">Nova igra</button>
</form>

% else:
<form action="/igra/" method="post">
    <input type="text" name="crka" autofocus>
    <button type="submit">Ugibaj!</button>
</form>

% end
