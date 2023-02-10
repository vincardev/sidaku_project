
tambahpensupp   = document.getElementById("tambahpensupp")
editpensupp     = document.getElementById("editpensupp")
modalpensupp    = document.getElementById("modalpensupp")

nmsuppdps          = document.getElementById("id_dps_nm_supp")
kualitasdps        = document.getElementById("id_dps_kualitas")
kirimdps           = document.getElementById("id_dps_pengiriman")
hargadps         = document.getElementById("id_dps_harga")

var strjson_pensupp = []

modalpensupp.addEventListener("click", function(){

    nmsuppdps.value = "";
    kualitasdps.value = "";
    kirimdps.value = "";
    hargadps.value = "";

    $("#editpensupp").hide();
    $("#tambahpensupp").show();
});

tambahpensupp.addEventListener("click", function(){

    data = {
        "id":"",
        "dps_nm_supp":nmsuppdps.value,
        "dps_kualitas":kualitasdps.value,
        "dps_pengiriman":kirimdps.value,
        "dps_harga":hargadps.value,
    }

    strjson_pensupp.push(data);
    ConvertToTablePensupp();

    $("#pensupp").text(JSON.stringify(strjson_pensupp));
    //jsonText.innerText = JSON.stringify(data)
});


function DeleteTablePensupp(index){
    strjson_pensupp.splice(index,1);
    ConvertToTablePensupp();
    $("#pensupp").text(JSON.stringify(strjson_pensupp));
}


function EditTablePensupp(index){
    
    nmsuppdps.value    = strjson_pensupp[index].dps_nm_supp;
    kualitasdps.value  = strjson_pensupp[index].dps_kualitas;
    kirimdps.value     = strjson_pensupp[index].dps_pengiriman;
    hargadps.value     = strjson_pensupp[index].dps_harga;

    idxinput.value = index;

    $("#editpensupp").show();
    $("#tambahpensupp").hide();
}


function EditDataPensupp(){

    idxinput = document.getElementById("idxinput")
    
    index = idxinput.value 
    strjson_pensupp[index].dps_nm_supp      = nmsuppdps.value;
    strjson_pensupp[index].dps_kualitas     = kualitasdps.value ;
    strjson_pensupp[index].dps_pengiriman   = kirimdps.value  ;
    strjson_pensupp[index].dps_harga        = hargadps.value  ;

    ConvertToTablePensupp();
    $("#pensupp").text(JSON.stringify(strjson_pensupp));
}

function ConvertToTablePensupp(){
    html ="";
    for (let i = 0; i < strjson_pensupp.length; i++) {
        html += "<tr>";
        html +=   "<td id='nmsuppdps-"+i+"'>"+ strjson_pensupp[i].dps_nm_supp+"</td>";
        html +=   "<td id='kualitasdps-"+i+"'>"+ strjson_pensupp[i].dps_kualitas+"</td>";
        html +=   "<td id='kirimdps-"+i+"'>"+ strjson_pensupp[i].dps_pengiriman+"</td>";
        html +=   "<td id='hargadps-"+i+"'>"+ strjson_pensupp[i].dps_harga+"</td>";
        html +=   "<td><button type='button' class='btn btn-sm btn-warning'  data-bs-toggle='modal' data-bs-target='#addpensupp' data-bs-whatever='Edit Data'  onclick='EditTablePensupp("+i+")'><i class='bi bi-pencil-square'></i></button> <button type='button' onclick='DeleteTablePensupp("+i+")' class='btn btn-sm btn-danger'><i class='bi bi-eraser-fill'></i></button></td>";
        html += "<tr>"; 
    }
    
    $(".tb-fill-pensupp").html(html);
}