
btntambah   = document.getElementById("btntambah")
btnedit     = document.getElementById("btnedit")
modalprod   = document.getElementById("modalprod")

var strjson = []

var file = {};

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

    fotoprod = document.getElementById("id_fotoprod").files;
    komoditiprod = document.getElementById("id_komoditi");
    volumeprod = document.getElementById("id_volume");
    satuanprod = document.getElementById("id_satuan");
    hargaprod = document.getElementById("id_harga");
    totalprod = document.getElementById("id_total");

    data = {
        "id":'',
        "foto":fotoprod,
        "komoditi":komoditiprod.value,
        "volume":volumeprod.value,
        "satuan":satuanprod.value,
        "harga":hargaprod.value,
        "total":totalprod.value,
        "url":''
    }

    strjson.push(data);
    ConvertToTable((strjson.length-1),true);
    readURL($("#id_fotoprod")[0].files, ".imgprod-"+(strjson.length-1));
    
    inputfile = $("#id_fotoprod")[0].files;    
    if (inputfile.length != 0){
        $("input[name='fotoprod-"+(strjson.length-1)+"']")[0].files= inputfile;
    }
    
    $("#jenprod").text(JSON.stringify(strjson));
    //jsonText.innerText = JSON.stringify(data)
});


function DeleteTable(index){

    $(".trindex-"+index).remove();
    for (let i = index; i < strjson.length; i++) {
        $(".trindex-"+i).removeClass('trindex-'+i).addClass('trindex-'+(i-1));
        $(".imgprod-"+i).removeClass('imgprod-'+i).addClass('imgprod-'+(i-1));
        $("#fotoprod-"+i).attr('id', "fotoprod-"+(i-1));
        $("#komoditi-"+i).attr('id', "komoditi-"+(i-1));
        $("#volume-"+i).attr('id', "volume-"+(i-1));
        $("#satuan-"+i).attr('id', "satuan-"+(i-1));
        $("#harga-"+i).attr('id', "harga-"+(i-1));
        $("#total-"+i).attr('id', "total-"+(i-1));
        $("#actionbtn-"+i).attr('id', "actionbtn-"+(i-1));

        $("input[name='fotoprod-"+i+"']").attr('name', "fotoprod-"+(i-1));
        $("input[name='komoditi-"+i+"']").attr('name', "komoditi-"+(i-1));
        $("input[name='volume-"+i+"']").attr('name', "volume-"+(i-1));
        $("input[name='satuan-"+i+"']").attr('name', "satuan-"+(i-1));
        $("input[name='harga-"+i+"']").attr('name', "harga-"+(i-1));
        $("input[name='total-"+i+"']").attr('name', "total-"+(i-1));

        html = "<button type='button' class='btn btn-sm btn-warning'  data-bs-toggle='modal' data-bs-target='#addprod' data-bs-whatever='Jenis Produk'  onclick='EditTable("+(i-1)+")'><i class='bi bi-pencil-square'></i></button> <button type='button' onclick='DeleteTable("+(i-1)+")' class='btn btn-sm btn-danger'><i class='bi bi-eraser-fill'></i></button>";
        $("#actionbtn-"+(i-1)).html(html)
        // console.log(i);
    }
    strjson.splice(index,1);

    // html += "<tr class='trindex-"+i+"'>";
    // // html +=   "<td id='fotoprod-"+i+"'>"+ "<input type='file' name='fotoprod-"+i+"' accept='image/png, image/jpeg, image/jpg' value='"+strjson[i].foto+"' >"+"</td>";
    // html +=   "<td id='fotoprod-"+i+"'>"+"<img class='img img-responsive' src='"+strjson[i].url+"' width='100' height='100'>"+"<input type='file' name='fotoprod-"+i+"' accept='image/png, image/jpeg, image/jpg' style='display:block' >"+"</td>";
    // html +=   "<td id='komoditi-"+i+"'>"+ strjson[i].komoditi+  "<input type='hidden'  name='komoditi-"+i+"' value='"+strjson[i].komoditi+"' />" +"</td>";
    // html +=   "<td id='volume-"+i+"'>"+ strjson[i].volume+ "<input type='hidden'  name='volume-"+i+"' value='"+strjson[i].volume+"' />"+"</td>";
    // html +=   "<td id='satuan-"+i+"'>"+ strjson[i].satuan+ "<input type='hidden'  name='satuan-"+i+"' value='"+strjson[i].satuan+"' />"+"</td>";
    // html +=   "<td id='harga-"+i+"'>"+ strjson[i].harga+ "<input type='hidden'  name='harga-"+i+"' value='"+strjson[i].harga+"' />"+"</td>";
    // html +=   "<td id='total-"+i+"'>"+ strjson[i].total+ "<input type='hidden'  name='total-"+i+"' value='"+strjson[i].total+"' />"+"</td>";
    // // html +=   "<td id='komoditi-"+i+"'>"+ strjson[i].komoditi+"</td>";
    // // html +=   "<td id='volume-"+i+"'>"+ strjson[i].volume+"</td>";
    // // html +=   "<td id='satuan-"+i+"'>"+ strjson[i].satuan+"</td>";
    // // html +=   "<td id='harga-"+i+"'>"+ strjson[i].harga+"</td>";
    // // html +=   "<td id='total-"+i+"'>"+ strjson[i].total+"</td>";
    // html +=   "<td><button type='button' class='btn btn-sm btn-warning'  data-bs-toggle='modal' data-bs-target='#addprod' data-bs-whatever='Jenis Produk'  onclick='EditTable("+i+")'><i class='bi bi-pencil-square'></i></button> <button type='button' onclick='DeleteTable("+i+")' class='btn btn-sm btn-danger'><i class='bi bi-eraser-fill'></i></button></td>";
    // html += "<tr>"; 
    // ConvertToTable();
    
    
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
    
    inputfile = $("input[name='fotoprod-"+index+"']")[0].files;
     
    $("#id_fotoprod")[0].files =inputfile;

    komoditiprod.value  = strjson[index].komoditi;
    volumeprod.value    = strjson[index].volume;
    satuanprod.value    = strjson[index].satuan;
    hargaprod.value     = strjson[index].harga;
    totalprod.value     = strjson[index].total;
    // fotoprod.files = 

    idxinput.value = index;

    $("#btnedit").show();
    $("#btntambah").hide();
}


function EditData(){

    fotoprod = document.getElementById("id_fotoprod").files;
    komoditiprod = document.getElementById("id_komoditi");
    volumeprod = document.getElementById("id_volume");
    satuanprod = document.getElementById("id_satuan");
    hargaprod = document.getElementById("id_harga");
    totalprod = document.getElementById("id_total");
    idxinput = document.getElementById("idxinput");
    
    index = idxinput.value 

    // $("input[name='fotoprod-"+index+"']")[0].files = $("#id_fotoprod")[0].files ;

    tmppath = readURL($("#id_fotoprod")[0].files, ".imgprod-"+index);
    
    strjson[index].foto = '';// JSON.stringify($("#id_fotoprod")[0].files);
    strjson[index].komoditi = komoditiprod.value ;
    strjson[index].volume = volumeprod.value  ;
    strjson[index].satuan = satuanprod.value  ;
    strjson[index].harga = hargaprod.value    ;
    strjson[index].total = totalprod.value    ;
    strjson[index].url = strjson[index].url   ;

    ConvertToTable(index);

    inputfile = $("#id_fotoprod")[0].files;
    
    if (inputfile.length != 0)
        $("input[name='fotoprod-"+index+"']")[0].files= inputfile;
    
    $("#jenprod").text(JSON.stringify(strjson));
}

function ConvertToTable(trindex = null,newpage = false){
    html ="";
    if (trindex == null){
        for (let i = 0; i < strjson.length; i++) {

            html += "<tr class='trindex-"+i+"'>";
            // html +=   "<td id='fotoprod-"+i+"'>"+ "<input type='file' name='fotoprod-"+i+"' accept='image/png, image/jpeg, image/jpg' value='"+strjson[i].foto+"' >"+"</td>";
            html +=   "<td id='fotoprod-"+i+"'>"+"<img class='img img-responsive imgprod-"+i+"' src='"+strjson[i].url+"' width='100' height='100'>"+"<input type='file' name='fotoprod-"+i+"' accept='image/png, image/jpeg, image/jpg' style='display:block' >"+"</td>";
            html +=   "<td id='komoditi-"+i+"'>"+ strjson[i].komoditi+  "<input type='hidden'  name='komoditi-"+i+"' value='"+strjson[i].komoditi+"' />" +"</td>";
            html +=   "<td id='volume-"+i+"'>"+ strjson[i].volume+ "<input type='hidden'  name='volume-"+i+"' value='"+strjson[i].volume+"' />"+"</td>";
            html +=   "<td id='satuan-"+i+"'>"+ strjson[i].satuan+ "<input type='hidden'  name='satuan-"+i+"' value='"+strjson[i].satuan+"' />"+"</td>";
            html +=   "<td id='harga-"+i+"'>"+ strjson[i].harga+ "<input type='hidden'  name='harga-"+i+"' value='"+strjson[i].harga+"' />"+"</td>";
            html +=   "<td id='total-"+i+"'>"+ strjson[i].total+ "<input type='hidden'  name='total-"+i+"' value='"+strjson[i].total+"' />"+"</td>";
            // html +=   "<td id='komoditi-"+i+"'>"+ strjson[i].komoditi+"</td>";
            // html +=   "<td id='volume-"+i+"'>"+ strjson[i].volume+"</td>";
            // html +=   "<td id='satuan-"+i+"'>"+ strjson[i].satuan+"</td>";
            // html +=   "<td id='harga-"+i+"'>"+ strjson[i].harga+"</td>";
            // html +=   "<td id='total-"+i+"'>"+ strjson[i].total+"</td>";
            html +=   "<td id='actionbtn-"+i+"'><button type='button' class='btn btn-sm btn-warning'  data-bs-toggle='modal' data-bs-target='#addprod' data-bs-whatever='Jenis Produk'  onclick='EditTable("+i+")'><i class='bi bi-pencil-square'></i></button> <button type='button' onclick='DeleteTable("+i+")' class='btn btn-sm btn-danger'><i class='bi bi-eraser-fill'></i></button></td>";
            html += "<tr>"; 
        }
        
        $(".tb-fill").html(html);
    }
    else {
        var i = trindex;

        if (newpage == true){
            // html += "<tr class='trindex-"+i+"'>";
        }
        html +=   "<td id='fotoprod-"+i+"'>"+"<img class='img img-responsive imgprod-"+i+"' src='"+strjson[i].url+"'  width='100' height='100'>"+ "<input type='file' name='fotoprod-"+i+"' accept='image/png, image/jpeg, image/jpg' style='display:block' >"+"</td>";
        // html +=   "<td id='fotoprod-"+i+"'>"+ "<input type='file' name='fotoprod-"+i+"' accept='image/png, image/jpeg, image/jpg' value='"+strjson[i].foto+"' >"+"</td>";
        html +=   "<td id='komoditi-"+i+"'>"+ strjson[i].komoditi+  "<input type='hidden'  name='komoditi-"+i+"' value='"+strjson[i].komoditi+"' />" +"</td>";
        html +=   "<td id='volume-"+i+"'>"+ strjson[i].volume+ "<input type='hidden'  name='volume-"+i+"' value='"+strjson[i].volume+"' />"+"</td>";
        html +=   "<td id='satuan-"+i+"'>"+ strjson[i].satuan+ "<input type='hidden'  name='satuan-"+i+"' value='"+strjson[i].satuan+"' />"+"</td>";
        html +=   "<td id='harga-"+i+"'>"+ strjson[i].harga+ "<input type='hidden'  name='harga-"+i+"' value='"+strjson[i].harga+"' />"+"</td>";
        html +=   "<td id='total-"+i+"'>"+ strjson[i].total+ "<input type='hidden'  name='total-"+i+"' value='"+strjson[i].total+"' />"+"</td>";
        // html +=   "<td id='komoditi-"+i+"'>"+ strjson[i].komoditi+"</td>";
        // html +=   "<td id='volume-"+i+"'>"+ strjson[i].volume+"</td>";
        // html +=   "<td id='satuan-"+i+"'>"+ strjson[i].satuan+"</td>";
        // html +=   "<td id='harga-"+i+"'>"+ strjson[i].harga+"</td>";
        // html +=   "<td id='total-"+i+"'>"+ strjson[i].total+"</td>";
        html +=   "<td id='actionbtn-"+i+"'><button type='button' class='btn btn-sm btn-warning'  data-bs-toggle='modal' data-bs-target='#addprod' data-bs-whatever='Jenis Produk'  onclick='EditTable("+i+")'><i class='bi bi-pencil-square'></i></button> <button type='button' onclick='DeleteTable("+i+")' class='btn btn-sm btn-danger'><i class='bi bi-eraser-fill'></i></button></td>";
       
        if (newpage == true){
            tag =  "<tr class='trindex-"+i+"'></tr>";
            $(".tb-fill").append(tag)
            $(".trindex-"+trindex).html(html);
        } else{
            $(".trindex-"+trindex).html(html);
        }

    }
}

function readURL(input, classstring) {
    // if (input.files && input.files[0]) {
    if (input.length != 0) {
        var reader = new FileReader();
        
        reader.onload = function (e) {
            $(classstring).attr('src', e.target.result);
            return e.target.result;
        }
        
        reader.readAsDataURL(input[0]);
    }
}


function GetUrlImageProduk (prod_id, index)
{
    var urlproduk = "{% url 'umkmdat:jsonprodukdata'  %}";

        $.ajax({
            url: urlproduk + "/"+prod_id,
            type: 'GET',
            dataType: "json",
        
            success : function (resp) {
                    // console.log(resp);
                    strjson[index].url =resp.prod_url;
            },
            error: function(){
            }
        });
    }