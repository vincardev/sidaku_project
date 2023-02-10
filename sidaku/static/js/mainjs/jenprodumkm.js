
btntambah   = document.getElementById("btntambah")
btnedit     = document.getElementById("btnedit")
modalprod   = document.getElementById("modalprod")

var strjson = []

modalprod.addEventListener("click", function(){

    fotoprod = document.getElementById("id_fotoprod")
    komoditiprod = document.getElementById("id_komoditi")
    volumeprod = document.getElementById("id_volume")
    satuanprod = document.getElementById("id_satuan")
    hargaprod = document.getElementById("id_harga")
    totalprod = document.getElementById("id_total")

    fotoprod.value = "";
    komoditiprod.value = "";
    volumeprod.value = "";
    satuanprod.value = "";
    hargaprod.value = "";
    totalprod.value = "";

    $("#btnedit").hide();
    $("#btntambah").show();
});

btntambah.addEventListener("click", function(){

    fotoprod = document.getElementById("id_fotoprod")
    komoditiprod = document.getElementById("id_komoditi")
    volumeprod = document.getElementById("id_volume")
    satuanprod = document.getElementById("id_satuan")
    hargaprod = document.getElementById("id_harga")
    totalprod = document.getElementById("id_total")
    

    data = {
        "id":"",
        "foto":fotoprod.value,
        "komoditi":komoditiprod.value,
        "volume":volumeprod.value,
        "satuan":satuanprod.value,
        "harga":hargaprod.value,
        "total":totalprod.value,
    }

    strjson.push(data);
    ConvertToTable();

    $("#jenprod").text(JSON.stringify(strjson));
    //jsonText.innerText = JSON.stringify(data)
});


function DeleteTable(index){
    strjson.splice(index,1);
    ConvertToTable();
    $("#jenprod").text(JSON.stringify(strjson));
}


function EditTable(index){

    fotoprod = document.getElementById("id_fotoprod")
    komoditiprod = document.getElementById("id_komoditi")
    volumeprod = document.getElementById("id_volume")
    satuanprod = document.getElementById("id_satuan")
    hargaprod = document.getElementById("id_harga")
    totalprod = document.getElementById("id_total")
    idxinput = document.getElementById("idxinput")
    
    fotoprod.src      = strjson[index].foto;
    komoditiprod.value  = strjson[index].komoditi;
    volumeprod.value    = strjson[index].volume;
    satuanprod.value    = strjson[index].satuan;
    hargaprod.value     = strjson[index].harga;
    totalprod.value     = strjson[index].total;

    idxinput.value = index;

    $("#btnedit").show();
    $("#btntambah").hide();
}


function EditData(){

    fotoprod = document.getElementById("id_fotoprod")
    komoditiprod = document.getElementById("id_komoditi")
    volumeprod = document.getElementById("id_volume")
    satuanprod = document.getElementById("id_satuan")
    hargaprod = document.getElementById("id_harga")
    totalprod = document.getElementById("id_total")
    idxinput = document.getElementById("idxinput")
    
    index = idxinput.value 
    strjson[index].foto = fotoprod.value;
    strjson[index].komoditi = komoditiprod.value ;
    strjson[index].volume = volumeprod.value  ;
    strjson[index].satuan = satuanprod.value  ;
    strjson[index].harga = hargaprod.value    ;
    strjson[index].total = totalprod.value    ;

    ConvertToTable();
    $("#jenprod").text(JSON.stringify(strjson));
}

function ConvertToTable(){
    html ="";
    for (let i = 0; i < strjson.length; i++) {
        html += "<tr>";
        html +=   "<td id='komoditi-"+i+"'>"+ strjson[i].komoditi+"</td>";
        html +=   "<td id='volume-"+i+"'>"+ strjson[i].volume+"</td>";
        html +=   "<td id='satuan-"+i+"'>"+ strjson[i].satuan+"</td>";
        html +=   "<td id='harga-"+i+"'>"+ strjson[i].harga+"</td>";
        html +=   "<td id='total-"+i+"'>"+ strjson[i].total+"</td>";
        html +=   "<td><button type='button' class='btn btn-sm btn-warning'  data-bs-toggle='modal' data-bs-target='#addprod' data-bs-whatever='Jenis Produk'  onclick='EditTable("+i+")'><i class='bi bi-pencil-square'></i></button> <button type='button' onclick='DeleteTable("+i+")' class='btn btn-sm btn-danger'><i class='bi bi-eraser-fill'></i></button></td>";
        html += "<tr>"; 
    }
    
    $(".tb-fill").html(html);
}