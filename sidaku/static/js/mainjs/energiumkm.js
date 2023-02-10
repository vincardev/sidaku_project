
tambahenergi   = document.getElementById("tambahenergi")
editenergi     = document.getElementById("editenergi")
modalenergi    = document.getElementById("modalenergi")

jnenergi       = document.getElementById("id_jen_energi")
kapasenergi       = document.getElementById("id_kapasitas")
ketenergi      = document.getElementById("id_keterangan")

var strjson_energi = []

modalenergi.addEventListener("click", function(){

    jnenergi.value = "";
    kapasenergi.value = "";
    ketenergi.value = "";

    $("#editenergi").hide();
    $("#tambahenergi").show();
});

tambahenergi.addEventListener("click", function(){

    data = {
        "id":"",
        "jen_energi":jnenergi.value,
        "kapasitas":kapasenergi.value,
        "keterangan":ketenergi.value,
    }

    strjson_energi.push(data);
    ConvertToTableEnergi();

    $("#dataenergi").text(JSON.stringify(strjson_energi));
    //jsonText.innerText = JSON.stringify(data)
});


function DeleteTableEnergi(index){
    strjson_energi.splice(index,1);
    ConvertToTableEnergi();
    $("#dataenergi").text(JSON.stringify(strjson_energi));
}


function EditTableEnergi(index){
    
    jnenergi.value    = strjson_energi[index].jen_energi;
    kapasenergi.value  = strjson_energi[index].kapasitas;
    ketenergi.value     = strjson_energi[index].keterangan;

    idxinput.value = index;

    $("#editenergi").show();
    $("#tambahenergi").hide();
}


function EditDataEnergi(){

    idxinput = document.getElementById("idxinput")
    
    index = idxinput.value 
    strjson_energi[index].jen_energi      = jnenergi.value;
    strjson_energi[index].kapasitas     = kapasenergi.value ;
    strjson_energi[index].keterangan   = ketenergi.value  ;

    ConvertToTableEnergi();
    $("#dataenergi").text(JSON.stringify(strjson_energi));
}

function ConvertToTableEnergi(){
    html ="";
    for (let i = 0; i < strjson_energi.length; i++) {
        html += "<tr>";
        html +=   "<td id='jen_energi-"+i+"'>"+ strjson_energi[i].jen_energi+"</td>";
        html +=   "<td id='kapasitas-"+i+"'>"+ strjson_energi[i].kapasitas+"</td>";
        html +=   "<td id='keterangan-"+i+"'>"+ strjson_energi[i].keterangan+"</td>";
        html +=   "<td><button type='button' class='btn btn-sm btn-warning'  data-bs-toggle='modal' data-bs-target='#addenergi' data-bs-whatever='Edit Data'  onclick='EditTableEnergi("+i+")'><i class='bi bi-pencil-square'></i></button> <button type='button' onclick='DeleteTableEnergi("+i+")' class='btn btn-sm btn-danger'><i class='bi bi-eraser-fill'></i></button></td>";
        html += "<tr>"; 
    }
    
    $(".tb-fill-energi").html(html);
}