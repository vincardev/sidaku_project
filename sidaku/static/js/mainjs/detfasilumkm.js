
tambahfasil   = document.getElementById("tambahfasil")
editfasil     = document.getElementById("editfasil")
modalfasil    = document.getElementById("modalfasil")

tipefasi       = document.getElementById("id_tipe_fasi")
nmfasi     = document.getElementById("id_nm_fasi")
thnfasi      = document.getElementById("id_thn_fasi")

var strjson_fasil = []

modalfasil.addEventListener("click", function(){

    tipefasi.value = "";
    nmfasi.value = "";
    thnfasi.value = "";

    $("#editfasil").hide();
    $("#tambahfasil").show();
});

tambahfasil.addEventListener("click", function(){

    data = {
        "id":"",
        "tipe_fasi":tipefasi.value,
        "nm_fasi":nmfasi.value,
        "thn_fasi":thnfasi.value,
    }

    strjson_fasil.push(data);
    ConvertToTablefasil();

    $("#fasildata").text(JSON.stringify(strjson_fasil));
    //jsonText.innerText = JSON.stringify(data)
});


function DeleteTablefasil(index){
    strjson_fasil.splice(index,1);
    ConvertToTablefasil();
    $("#fasildata").text(JSON.stringify(strjson_fasil));
}


function EditTablefasil(index){
    
    tipefasi.value    = strjson_fasil[index].tipe_fasi;
    nmfasi.value  = strjson_fasil[index].nm_fasi;
    thnfasi.value   = strjson_fasil[index].thn_fasi;

    idxinput.value = index;

    $("#editfasil").show();
    $("#tambahfasil").hide();
}


function EditDatafasil(){

    idxinput = document.getElementById("idxinput")
    
    index = idxinput.value 
    strjson_fasil[index].tipe_fasi      = tipefasi.value;
    strjson_fasil[index].nm_fasi     = nmfasi.value ;
    strjson_fasil[index].thn_fasi   = thnfasi.value  ;

    ConvertToTablefasil();
    $("#fasildata").text(JSON.stringify(strjson_fasil));
}

function ConvertToTablefasil(){
    html ="";
    for (let i = 0; i < strjson_fasil.length; i++) {
        html += "<tr>";
        html +=   "<td id='tipe_fasi-"+i+"'>"+ strjson_fasil[i].tipe_fasi+"</td>";
        html +=   "<td id='nm_fasi-"+i+"'>"+ strjson_fasil[i].nm_fasi+"</td>";
        html +=   "<td id='thn_fasi-"+i+"'>"+ strjson_fasil[i].thn_fasi+"</td>";
        html +=   "<td><button type='button' class='btn btn-sm btn-warning'  data-bs-toggle='modal' data-bs-target='#addfasil' data-bs-whatever='Edit Data'  onclick='EditTablefasil("+i+")'><i class='bi bi-pencil-square'></i></button> <button type='button' onclick='DeleteTablefasil("+i+")' class='btn btn-sm btn-danger'><i class='bi bi-eraser-fill'></i></button></td>";
        html += "<tr>"; 
    }
    
    $(".tb-fill-fasil").html(html);
}