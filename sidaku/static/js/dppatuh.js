
    var kertaskerjaArray = [];
    var kkProfileRisikoArray = [];
    
    function addKertasKerjatoArray(clsname)   {
        kertaskerjaArray.push(clsname);
    } 
    
    function addProfileRisikoArray(clsname)   {
        kkProfileRisikoArray.push(clsname);
    } 

    function getPerhitunganKertaskerja()   {

        var nilaikredittotal=0;
        var bobottotal=0;
        var allscoretotal=0;


        var totallastscore=0;

        for (b = 0; b < kertaskerjaArray.length; b++)
        {
            var dataclass = $('.'+kertaskerjaArray[b]).map((_,el) => el.value).get();
            var total = 0;
            for (i = 0; i < dataclass.length; i++){
                total += parseInt(dataclass[i]);
            }
            var hitungtext =
            "<table class='table table-borderless  table-sm  '>"+
                "<tbody>"+
                    "<tr>"+
                        "<td class='text-center  border-bottom border-3 border-dark'>"+total+"</td>"+
                        "<td class='text-center'>X</td>"+
                        "<td class='text-center'>100%</td>"+
                   " </tr>"+
                    "<tr>"+
                        "<td class='text-center'>"+ dataclass.length +"</td>"+
                        "<td class='text-center'></td>"+
                        "<td class='text-center'></td>"+
                    "</tr>"+
                "</tbody>"+
            "</table>";

            var ratio = total/dataclass.length * 100;

            var nilaikredit = 0;
            if (ratio <= 25){
                nilaikredit = 4;
            } else if (ratio <= 50){
                nilaikredit = 3;
            } else if (ratio <= 75){
                nilaikredit = 2;
            } else if (ratio <= 100){
                nilaikredit = 1;
            }


            var bobot = 1;

            var score = 0;
            if (nilaikredit == 4){
                score = 1;
            } else if (nilaikredit == 3){
                score = 2;
            } else if (nilaikredit == 2){
                score = 3;
            } else if (nilaikredit == 1){
                score = 4;
            }
            
            $("#hitung-"+kertaskerjaArray[b]).html(hitungtext);
            $("#ratio-"+kertaskerjaArray[b]).html(ratio.toFixed(2) + '%');
            $("#nilai-"+kertaskerjaArray[b]).text(nilaikredit);
            $("#bobot-"+kertaskerjaArray[b]).text(bobot);
            $("#lastscore-"+kertaskerjaArray[b]).text(score);
            
            
            $("#hratio-"+kertaskerjaArray[b]).html(ratio.toFixed(2) + '%');
            $("#hnilai-"+kertaskerjaArray[b]).text(nilaikredit);
            $("#hskor-"+kertaskerjaArray[b]).text(score);
            $("#hkriteria-"+kertaskerjaArray[b]).text(cekkriteriasehat(score));

            
            totallastscore += score;
            
            nilaikredittotal += nilaikredit;
            bobottotal += bobot;
        }


        for (b = 0; b < kertaskerjaArray.length; b++)
        {
            var clname = kertaskerjaArray[b].split('_')
            var hratios = $(".hratio-"+clname[0]+"_"+clname[1]);
            var hnilais = $(".hnilai-"+clname[0]+"_"+clname[1]);
            var hskors = $(".hskor-"+clname[0]+"_"+clname[1]);
            var hkriterias = $(".hkriteria-"+clname[0]+"_"+clname[1]);

            var totalnilai=0;

            $(".hnilai-"+clname[0]+"_"+clname[1]).each(function(){
                totalnilai += parseInt($(this).text());
            });

            var totalskor=0;
            $(".hskor-"+clname[0]+"_"+clname[1]).each(function(){
                totalskor += parseInt($(this).text());
            });

            $("#hratio-"+clname[1]).html(totalnilai);
            $("#hnilai-"+clname[1]).html((totalnilai/hnilais.length).toFixed(2));
            $("#hskor-"+clname[1]).html((totalskor/ (hskors.length*4) * 100).toFixed(2));
            $("#hkriteria-"+clname[1]).html(cekpengawasan(parseFloat($("#hskor-"+clname[1]).text())) );
        }

        var totalhratio = 0;
        $(".hratio-tata-kelola-total").each(function(){
            totalhratio += parseInt($(this).text());
        });
        
        var totalhskor = 0;
        $(".hskor-tata-kelola-sub").each(function(){
            totalhskor += parseInt($(this).text());
        });

        $("#hratio-tata-kelola").text(totalhratio);
        $("#hnilai-tata-kelola").text((totalhratio/$(".hratio-tata-kelola-sub").length).toFixed(2));
        $("#hskor-tata-kelola").text( (totalhskor/ ($(".hskor-tata-kelola-sub").length*4) * 100).toFixed(2) );
        $("#hkriteria-tata-kelola").text(cekpengawasan(parseFloat($("#hskor-tata-kelola").text())) );
        

        
        var nilaikreditTotal = totallastscore/(kertaskerjaArray.length*4)*100;
        var bobottatakelola = 30;
        var scoretatakelola = nilaikreditTotal*bobottatakelola/100;
        $("#nilai-tata-kelola").text(nilaikreditTotal.toFixed(5));
        $("#bobot-tata-kelola").text(bobottatakelola + '(%)');
        $("#lastscore-tata-kelola").text(scoretatakelola.toFixed(5));

        allscoretotal += totallastscore;




        totallastscore=0;

        for (b = 0; b < kkProfileRisikoArray.length; b++)
        {
            var dataclass = $('.'+kkProfileRisikoArray[b]).map((_,el) => el.value).get();
            var total = 0;
            for (i = 0; i < dataclass.length; i++){
                total += parseInt(dataclass[i]);
            }
            var hitungtext =
            "<table class='table table-borderless  table-sm  '>"+
                "<tbody>"+
                    "<tr>"+
                        "<td class='text-center  border-bottom border-3 border-dark'>"+total+"</td>"+
                        "<td class='text-center'>X</td>"+
                        "<td class='text-center'>100%</td>"+
                   " </tr>"+
                    "<tr>"+
                        "<td class='text-center'>"+ dataclass.length +"</td>"+
                        "<td class='text-center'></td>"+
                        "<td class='text-center'></td>"+
                    "</tr>"+
                "</tbody>"+
            "</table>";

            var ratio = total/dataclass.length * 100;

            var nilaikredit = 0;
            if (ratio <= 25){
                nilaikredit = 4;
            } else if (ratio <= 50){
                nilaikredit = 3;
            } else if (ratio <= 75){
                nilaikredit = 2;
            } else if (ratio <= 100){
                nilaikredit = 1;
            }
            var bobot = 1;

            var score = 0;
            if (nilaikredit == 4){
                score = 1;
            } else if (nilaikredit == 3){
                score = 2;
            } else if (nilaikredit == 2){
                score = 3;
            } else if (nilaikredit == 1){
                score = 4;
            }
            
            $("#hitung-"+kkProfileRisikoArray[b]).html(hitungtext);
            $("#ratio-"+kkProfileRisikoArray[b]).html(ratio.toFixed(2) + '%');
            $("#nilai-"+kkProfileRisikoArray[b]).text(nilaikredit);
            $("#bobot-"+kkProfileRisikoArray[b]).text(bobot);
            $("#lastscore-"+kkProfileRisikoArray[b]).text(score);



            $("#hratio-"+kkProfileRisikoArray[b]).html(ratio.toFixed(2) + '%');
            $("#hnilai-"+kkProfileRisikoArray[b]).text(nilaikredit);
            $("#hskor-"+kkProfileRisikoArray[b]).text(score);
            $("#hkriteria-"+kkProfileRisikoArray[b]).text(cekkriteriasehat(score));
            

            totallastscore += score;
            
            nilaikredittotal += nilaikredit;
            bobottotal += bobot;
        }

        var dataasprototal = calasprototal();
        var datapinjasprod = calpinjasprod();
        var dataaliktotal = calaliktotal();
        var dataalikwajib = calalikwajib();

        totallastscore += dataasprototal[3];
        totallastscore += datapinjasprod[3];
        totallastscore += dataaliktotal[3];
        totallastscore += dataalikwajib[3];

        allscoretotal += totallastscore;

        nilaikredittotal += dataasprototal[1];
        nilaikredittotal += datapinjasprod[1];
        nilaikredittotal += dataaliktotal[1];
        nilaikredittotal += dataalikwajib[1];

        bobottotal += dataasprototal[2];
        bobottotal += datapinjasprod[2];
        bobottotal += dataaliktotal[2];
        bobottotal += dataalikwajib[2];


        $("#hratio-risiko-pinjaman").html((dataasprototal[1]+datapinjasprod[1]));
        $("#hnilai-risiko-pinjaman").html((dataasprototal[1]+datapinjasprod[1])/2);
        $("#hskor-risiko-pinjaman").html((dataasprototal[3]+datapinjasprod[3])/(4*2)*100);
        $("#hkriteria-risiko-pinjaman").html(cekpengawasan(parseFloat($("#hskor-risiko-pinjaman").text())));


        for (b = 0; b < kkProfileRisikoArray.length; b++)
        {
            var clname = kkProfileRisikoArray[b].split('_')
            var hratios = $(".hratio-"+clname[0]+"_"+clname[1]);
            var hnilais = $(".hnilai-"+clname[0]+"_"+clname[1]);
            var hskors = $(".hskor-"+clname[0]+"_"+clname[1]);
            var hkriterias = $(".hkriteria-"+clname[0]+"_"+clname[1]);

            var totalnilai=0;

            $(".hnilai-"+clname[0]+"_"+clname[1]).each(function(){
                totalnilai += parseInt($(this).text());
            });

            var totalskor=0;
            $(".hskor-"+clname[0]+"_"+clname[1]).each(function(){
                totalskor += parseInt($(this).text());
            });

            $("#hratio-"+clname[1]).html(totalnilai);
            $("#hnilai-"+clname[1]).html((totalnilai/hnilais.length).toFixed(2));
            $("#hskor-"+clname[1]).html((totalskor/ (hskors.length*4) * 100).toFixed(2));
            $("#hkriteria-"+clname[1]).html(cekpengawasan(parseFloat($("#hskor-"+clname[1]).text())) );


        }



        var totalhratio = 0;
        $(".hratio-profil-risiko-total").each(function(){
            totalhratio += parseInt($(this).text());
        });
        
        var totalhskor = 0;
        $(".hskor-profil-risiko-sub").each(function(){
            totalhskor += parseInt($(this).text());
        });

        $("#hratio-profil-risiko").text(totalhratio);
        $("#hnilai-profil-risiko").text((totalhratio/$(".hratio-profil-risiko-sub").length).toFixed(2));
        $("#hskor-profil-risiko").text( (totalhskor/ ($(".hskor-profil-risiko-sub").length*4) * 100).toFixed(2) );
        $("#hkriteria-profil-risiko").text(cekpengawasan(parseFloat($("#hskor-profil-risiko").text())) );
        


// SUB RISIKO INHEREN
        $(".hnilai-sub-risiko-inheren").each(function(){
            var data =  $("#hratio-risiko-inheren").text();
            if(data == "" ) { data = 0; }
            data = parseInt(data) +  parseInt($(this).text());
            $("#hratio-risiko-inheren").text(data);
            $("#hnilai-risiko-inheren").text((data/ $(".hratio-sub-risiko-inheren").length).toFixed(2));
        });

        $(".hskor-sub-risiko-inheren").each(function(){
            var data =  $("#hkriteria-risiko-inheren").text();
            if(data == "" ) { data = 0; }
            data = parseInt(data) +  parseInt($(this).text());
            $("#hkriteria-risiko-inheren").text(data);
            $("#hskor-risiko-inheren").text((data/ ($(".hskor-sub-risiko-inheren").length * 4) * 100).toFixed(2));
        });
        $("#hkriteria-risiko-inheren").text(cekpengawasan(parseFloat($("#hskor-risiko-inheren").text())) );
        

//SUB MANAJEMEN RESIKO
        $(".hnilai-sub-kualitas-manajemen-risiko").each(function(){
            var data =  $("#hratio-kualitas-manajemen-risiko").text();
            if(data == "" ) { data = 0; }
            data = parseInt(data) +  parseInt($(this).text());
            $("#hratio-kualitas-manajemen-risiko").text(data);
            $("#hnilai-kualitas-manajemen-risiko").text((data/ $(".hratio-sub-kualitas-manajemen-risiko").length).toFixed(2));
        });

        $(".hskor-sub-kualitas-manajemen-risiko").each(function(){
            var data =  $("#hkriteria-kualitas-manajemen-risiko").text();
            if(data == "" ) { data = 0; }
            data = parseInt(data) +  parseInt($(this).text());
            $("#hkriteria-kualitas-manajemen-risiko").text(data);
            $("#hskor-kualitas-manajemen-risiko").text((data/ ($(".hskor-sub-kualitas-manajemen-risiko").length * 4) * 100).toFixed(2));
        });
        $("#hkriteria-kualitas-manajemen-risiko").text(cekpengawasan(parseFloat($("#hskor-kualitas-manajemen-risiko").text())) );
        
        


        addnilaikredit = 4;
        nilaikreditTotal = totallastscore/((kkProfileRisikoArray.length+addnilaikredit)*4)*100;
        var bobotprofilrisiko = 15;
        var scoreprofilrisiko = nilaikreditTotal*bobotprofilrisiko/100;
        $("#nilai-profil-risiko").text(nilaikreditTotal.toFixed(5));
        $("#bobot-profil-risiko").text(bobotprofilrisiko + '(%)');
        $("#lastscore-profil-risiko").text(scoreprofilrisiko.toFixed(5));









        var nilaikreditkinerja= 0;
        var kinerjalastscore= 0;

        var datarentaset = calrentaset();
        var datarentekuitas = calrentekuitas();
        var datamandiriop = calmandiriop();
        var databodanpo = calbodanpo();
        var databudanshuk = calbudanshuk();
        var datapdadantp = calpdadantp();
        var datapbmdantp = calpbmdantp();
        var datacdrsisk = calcdrsisk();
        var datakasbankkjp = calkasbankkjp();
        var datapiutangdanaterima = calpiutangdanaterima();
        var dataasetlancarwajibjp = calasetlancarwajibjp();
        var datatumbuhaset = caltumbuhaset();
        var datatumbuhdanaditerima = caltumbuhdanaditerima();
        var datatumbuhekuitas = caltumbuhekuitas();
        var datatumbuhhasilusahabersih = caltumbuhhasilusahabersih();
        var datapdptutamatotalpdpt = calpdptutamatotalpdpt();
        var datashbersihsps = calshbersihsps();
        var datapartisipasisimagt = calpartisipasisimagt();

        kinerjalastscore += datarentaset[3];
        kinerjalastscore += datarentekuitas[3];
        kinerjalastscore += datamandiriop[3];
        kinerjalastscore += databodanpo[3];
        kinerjalastscore += databudanshuk[3];

        kinerjalastscore += datapdadantp[3];
        kinerjalastscore += datapbmdantp[3];
        kinerjalastscore += datacdrsisk[3];

        kinerjalastscore += datakasbankkjp[3];
        kinerjalastscore += datapiutangdanaterima[3];
        kinerjalastscore += dataasetlancarwajibjp[3];

        kinerjalastscore += datatumbuhaset[3];
        kinerjalastscore += datatumbuhdanaditerima[3];
        kinerjalastscore += datatumbuhekuitas[3];
        kinerjalastscore += datatumbuhhasilusahabersih[3];
        kinerjalastscore += datapdptutamatotalpdpt[3];
        kinerjalastscore += datashbersihsps[3];
        kinerjalastscore += datapartisipasisimagt[3];


        allscoretotal += kinerjalastscore;

        nilaikredittotal += datarentaset[1];
        nilaikredittotal += datarentekuitas[1];
        nilaikredittotal += datamandiriop[1];
        nilaikredittotal += databodanpo[1];
        nilaikredittotal += databudanshuk[1];
        nilaikredittotal += datapdadantp[1];
        nilaikredittotal += datapbmdantp[1];
        nilaikredittotal += datacdrsisk[1];
        nilaikredittotal += datakasbankkjp[1];
        nilaikredittotal += datapiutangdanaterima[1];
        nilaikredittotal += dataasetlancarwajibjp[1];
        nilaikredittotal += datatumbuhaset[1];
        nilaikredittotal += datatumbuhdanaditerima[1];
        nilaikredittotal += datatumbuhekuitas[1];
        nilaikredittotal += datatumbuhhasilusahabersih[1];
        nilaikredittotal += datapdptutamatotalpdpt[1];
        nilaikredittotal += datashbersihsps[1];
        nilaikredittotal += datapartisipasisimagt[1];

        bobottotal += datarentaset[2];
        bobottotal += datarentekuitas[2];
        bobottotal += datamandiriop[2];
        bobottotal += databodanpo[2];
        bobottotal += databudanshuk[2];
        bobottotal += datapdadantp[2];
        bobottotal += datapbmdantp[2];
        bobottotal += datacdrsisk[2];
        bobottotal += datakasbankkjp[2];
        bobottotal += datapiutangdanaterima[2];
        bobottotal += dataasetlancarwajibjp[2];
        bobottotal += datatumbuhaset[2];
        bobottotal += datatumbuhdanaditerima[2];
        bobottotal += datatumbuhekuitas[2];
        bobottotal += datatumbuhhasilusahabersih[2];
        bobottotal += datapdptutamatotalpdpt[2];
        bobottotal += datashbersihsps[2];
        bobottotal += datapartisipasisimagt[2];


        nilaikreditkinerja = kinerjalastscore/(18*4)*100;
        var bobotkinerja = 40;
        var scorekinerja = nilaikreditkinerja*bobotkinerja/100;
        $("#nilai-kinerja").text(nilaikreditkinerja.toFixed(5));
        $("#bobot-kinerja").text(bobotkinerja + '(%)');
        $("#lastscore-kinerja").text(scorekinerja.toFixed(5));
       

        //EVALUASI
        $("#hratio-child-eval-1").text(parseInt(datarentaset[1]+datarentekuitas[1]+datamandiriop[1]));
        $("#hnilai-child-eval-1").text((parseInt(datarentaset[1]+datarentekuitas[1]+datamandiriop[1])/3).toFixed(2));
        $("#hskor-child-eval-1").text( (parseInt(datarentaset[3]+datarentekuitas[3]+datamandiriop[3])/(3*4) * 100).toFixed(2) );
        $("#hkriteria-child-eval-1").text(cekpengawasan(parseFloat($("#hskor-child-eval-1").text())));
        
        $("#hratio-child-eval-2").text(parseInt(databodanpo[1]+databudanshuk[1]));
        $("#hnilai-child-eval-2").text((parseInt(databodanpo[1]+databudanshuk[1])/2).toFixed(2));
        $("#hskor-child-eval-2").text( (parseInt(databodanpo[3]+databudanshuk[3])/(2*4) * 100).toFixed(2) );
        $("#hkriteria-child-eval-2").text(cekpengawasan(parseFloat($("#hskor-child-eval-2").text())));

        $("#hratio-eval").text(parseInt( $("#hratio-child-eval-1").text())+ parseInt( $("#hratio-child-eval-2").text()));
        $("#hnilai-eval").text((parseInt( $("#hratio-eval").text())/5).toFixed(2));
        $("#hskor-eval").text( ((parseInt(datarentaset[3]+datarentekuitas[3]+datamandiriop[3]+databodanpo[3]+databudanshuk[3]))/(5*4) * 100).toFixed(2) );
        $("#hkriteria-eval").text(cekpengawasan(parseFloat($("#hskor-eval").text())));
        


        //MANAJEMEN UANG
        $("#hratio-child-manung-1").text(parseInt(datapdadantp[1]+datapbmdantp[1]+datacdrsisk[1]));
        $("#hnilai-child-manung-1").text((parseInt(datapdadantp[1]+datapbmdantp[1]+datacdrsisk[1])/3).toFixed(2));
        $("#hskor-child-manung-1").text( (parseInt(datapdadantp[3]+datapbmdantp[3]+datacdrsisk[3])/(3*4) * 100).toFixed(2) );
        $("#hkriteria-child-manung-1").text(cekpengawasan(parseFloat($("#hskor-child-manung-1").text())));
        


        $("#hratio-child-manung-2").text(parseInt(datakasbankkjp[1]+datapiutangdanaterima[1]+dataasetlancarwajibjp[1]));
        $("#hnilai-child-manung-2").text((parseInt(datakasbankkjp[1]+datapiutangdanaterima[1]+dataasetlancarwajibjp[1])/3).toFixed(2));
        $("#hskor-child-manung-2").text( (parseInt(datakasbankkjp[3]+datapiutangdanaterima[3]+dataasetlancarwajibjp[3])/(3*4) * 100).toFixed(2) );
        $("#hkriteria-child-manung-2").text(cekpengawasan(parseFloat($("#hskor-child-manung-2").text())));
        

        $("#hratio-manung").text(parseInt( $("#hratio-child-manung-1").text())+ parseInt( $("#hratio-child-manung-2").text()));
        $("#hnilai-manung").text((parseInt( $("#hratio-manung").text())/6).toFixed(2));
        $("#hskor-manung").text( ((parseInt(datapdadantp[3]+datapbmdantp[3]+datacdrsisk[3] + datakasbankkjp[3]+datapiutangdanaterima[3]+dataasetlancarwajibjp[3]))/(6*4) * 100).toFixed(2) );
        $("#hkriteria-manung").text(cekpengawasan(parseFloat($("#hskor-manung").text())));
        

        //SINAMBUNG 

        $("#hratio-child-nambung-1").text(parseInt(datatumbuhaset[1]+datatumbuhdanaditerima[1]+datatumbuhekuitas[1]+datatumbuhhasilusahabersih[1]));
        $("#hnilai-child-nambung-1").text((parseInt(datatumbuhaset[1]+datatumbuhdanaditerima[1]+datatumbuhekuitas[1]+datatumbuhhasilusahabersih[1])/4).toFixed(2));
        $("#hskor-child-nambung-1").text( (parseInt(datatumbuhaset[3]+datatumbuhdanaditerima[3]+datatumbuhekuitas[3]+datatumbuhhasilusahabersih[3])/(4*4) * 100).toFixed(2) );
        $("#hkriteria-child-nambung-1").text(cekpengawasan(parseFloat($("#hskor-child-nambung-1").text())));
        


        $("#hratio-child-nambung-2").text(parseInt(datapdptutamatotalpdpt[1]+datashbersihsps[1]+datapartisipasisimagt[1]));
        $("#hnilai-child-nambung-2").text((parseInt(datapdptutamatotalpdpt[1]+datashbersihsps[1]+datapartisipasisimagt[1])/3).toFixed(2));
        $("#hskor-child-nambung-2").text( (parseInt(datapdptutamatotalpdpt[3]+datashbersihsps[3]+datapartisipasisimagt[3])/(3*4) * 100).toFixed(2) );
        $("#hkriteria-child-nambung-2").text(cekpengawasan(parseFloat($("#hskor-child-nambung-2").text())));
        

        $("#hratio-nambung").text(parseInt( $("#hratio-child-nambung-1").text())+ parseInt( $("#hratio-child-nambung-2").text()));
        $("#hnilai-nambung").text((parseInt( $("#hratio-nambung").text())/7).toFixed(2));
        $("#hskor-nambung").text( 
            ((parseInt(datatumbuhaset[3]+datatumbuhdanaditerima[3]+datatumbuhekuitas[3]+datatumbuhhasilusahabersih[3] +
            datapdptutamatotalpdpt[3]+datashbersihsps[3]+datapartisipasisimagt[3]))/(7*4) * 100).toFixed(2) );
        $("#hkriteria-nambung").text(cekpengawasan(parseFloat($("#hskor-nambung").text())));
        

        //KINERJA
        $("#hratio-kinerja").text( (parseInt( $("#hratio-eval").text()) + parseInt( $("#hratio-manung").text()) + parseInt( $("#hratio-nambung").text())) );
        $("#hnilai-kinerja").text((parseInt( $("#hratio-kinerja").text())/18).toFixed(2));
        $("#hskor-kinerja").text( 
            ((parseInt( 
                datarentaset[3]+datarentekuitas[3]+datamandiriop[3]+databodanpo[3]+databudanshuk[3]+
                datapdadantp[3]+datapbmdantp[3]+datacdrsisk[3] + datakasbankkjp[3]+datapiutangdanaterima[3]+dataasetlancarwajibjp[3]+
                datatumbuhaset[3]+datatumbuhdanaditerima[3]+datatumbuhekuitas[3]+datatumbuhhasilusahabersih[3] +
            datapdptutamatotalpdpt[3]+datashbersihsps[3]+datapartisipasisimagt[3])
            )/(18*4) * 100).toFixed(2) 
        );
        $("#hkriteria-kinerja").text(cekpengawasan(parseFloat($("#hskor-kinerja").text())));
        

        //PERMODALAN
       
        var nilaikreditmodal= 0;
        var modallastscore= 0;

        var dataekuitastotalaset = calekuitastotalaset();
        var datacukupmodal =   calcukupmodal();
        var datamodalpinjamaset = calmodalpinjamaset();
        var datawjbjkpekuitas = calwjbjkpekuitas();

        modallastscore += dataekuitastotalaset[3];
        modallastscore += datacukupmodal[3];
        modallastscore += datamodalpinjamaset[3];
        modallastscore += datawjbjkpekuitas[3];

        allscoretotal += modallastscore;

        nilaikredittotal += dataekuitastotalaset[1];
        nilaikredittotal += datacukupmodal[1];
        nilaikredittotal += datamodalpinjamaset[1];
        nilaikredittotal += datawjbjkpekuitas[1];

        bobottotal += calekuitastotalaset[2];
        bobottotal += calcukupmodal[2];
        bobottotal += calmodalpinjamaset[2];
        bobottotal += calwjbjkpekuitas[2];

        nilaikreditmodal = modallastscore/(4*4)*100;
        var bobotmodal = 15;
        var scoremodal = nilaikreditmodal*bobotmodal/100;
        $("#nilai-modal").text(nilaikreditmodal.toFixed(5));
        $("#bobot-modal").text(bobotmodal + '(%)');
        $("#lastscore-modal").text(scoremodal.toFixed(5));


        $("#nilaikredit-total").text(nilaikredittotal);
        $("#bobot-total").text((nilaikredittotal/60).toFixed(5));

        allscoretotal = parseFloat($("#lastscore-modal").text()) + parseFloat($("#lastscore-kinerja").text()) 
                        + parseFloat($("#lastscore-profil-risiko").text())+ parseFloat($("#lastscore-tata-kelola").text());
        $("#lastscore-total").text(allscoretotal);


        
        $("#hratio-child-modal-1").text(parseInt(dataekuitastotalaset[1]+datacukupmodal[1]));
        $("#hnilai-child-modal-1").text((parseInt(dataekuitastotalaset[1]+datacukupmodal[1])/2).toFixed(2));
        $("#hskor-child-modal-1").text( (parseInt(dataekuitastotalaset[3]+datacukupmodal[3])/(2*4) * 100).toFixed(2) );
        $("#hkriteria-child-modal-1").text(cekpengawasan(parseFloat($("#hskor-child-modal-1").text())));
        
        $("#hratio-child-modal-2").text(parseInt(datamodalpinjamaset[1]+datawjbjkpekuitas[1]));
        $("#hnilai-child-modal-2").text((parseInt(datamodalpinjamaset[1]+datawjbjkpekuitas[1])/2).toFixed(2));
        $("#hskor-child-modal-2").text( (parseInt(datamodalpinjamaset[3]+datawjbjkpekuitas[3])/(2*4) * 100).toFixed(2) );
        $("#hkriteria-child-modal-2").text(cekpengawasan(parseFloat($("#hskor-child-modal-2").text())));
        

        $("#hratio-modal").text(parseInt( $("#hratio-child-modal-1").text())+ parseInt( $("#hratio-child-modal-2").text()));
        $("#hnilai-modal").text((parseInt( $("#hratio-modal").text())/4).toFixed(2));
        $("#hskor-modal").text( ((parseInt(dataekuitastotalaset[3] + datacukupmodal[3] + datamodalpinjamaset[3] + datawjbjkpekuitas[3]))/(4*4) * 100).toFixed(2) );
        $("#hkriteria-modal").text(cekpengawasan(parseFloat($("#hskor-modal").text())));
        
        
        var profskor = parseFloat($("#hskor-profil-risiko").text());
        var profsubtot = profskor * parseFloat($("#profil-risiko-pros").text())/100;
        $("#profil-risiko-skortot").text(profskor);
        $("#profil-risiko-subtot").text(profsubtot.toFixed(2));

        var takelskor = parseFloat($("#hskor-tata-kelola").text());
        var takelsubtot = takelskor * parseFloat($("#tata-kelola-pros").text())/100;
        $("#tata-kelola-skortot").text(takelskor);
        $("#tata-kelola-subtot").text(takelsubtot.toFixed(2));

        var kinerjaskor = parseFloat($("#hskor-kinerja").text());
        var kinerjasubtot = kinerjaskor * parseFloat($("#kinerja-pros").text())/100;
        $("#kinerja-skortot").text(kinerjaskor);
        $("#kinerja-subtot").text(kinerjasubtot.toFixed(2));

        var modalskor = parseFloat($("#hskor-modal").text());
        var modalsubtot = modalskor * parseFloat($("#modal-pros").text())/100;
        $("#modal-skortot").text(modalskor);
        $("#modal-subtot").text(modalsubtot.toFixed(2));

        var jumlahpros = '100%';
        var jumlahsubtot = profsubtot+takelsubtot+kinerjasubtot+modalsubtot;
        $("#jumlah-pros").text(jumlahpros);
        $("#jumlah-subtot").text(jumlahsubtot.toFixed(2));



        //Predikat 

        $("#hratio-predikat").text(parseInt( $("#hratio-modal").text())+ parseInt( $("#hratio-kinerja").text())+parseInt( $("#hratio-profil-risiko").text())+ parseInt( $("#hratio-tata-kelola").text()));
        $("#hnilai-predikat").text((parseInt( $("#hratio-predikat").text())/60).toFixed(2));
        $("#hskor-predikat").text(jumlahsubtot);
        $("#hkriteria-predikat").text(cekpengawasan(parseFloat($("#hskor-predikat").text())));
        //console.log(calasprototal()[3]);
    } 

    function cekpengawasan(skor){
        var kriteria = "";
        if (skor >= 0 && skor < 51){
            kriteria = "DALAM PENGAWASAN KHUSUS";
        } else if (skor >= 51 && skor < 66){
            kriteria = "DALAM PENGAWASAN";
        } else if ( skor >= 66 && skor < 80){
            kriteria = "CUKUP SEHAT";
        } else if (skor >= 80){
            kriteria = "SEHAT";
        }
        return kriteria;
    }

    function cekkriteriasehat(skor){
        var kriteria = "";
        if (skor == 1){
            kriteria = "TIDAK SEHAT";
        } else if (skor == 2){
            kriteria = "KURANG SEHAT";
        } else if ( skor == 3){
            kriteria = "CUKUP SEHAT";
        } else if (skor == 4){
            kriteria = "SEHAT";
        }
        return kriteria;
    }


    function calasprototal(){
        var title1= 'Aset Produktif	';
        var title2= ' Total Aset 	';
        var value1 = $("input[name='lpk_asetprod']").val();
        var value2 = $("input[name='lpk_totaset']").val();
        var tabletext = gettabletext(title1, value1, title2, value2);

        var ratio = Math.ceil(value1/value2 * 100) ;
        var nilaikredit =0;
        if (ratio <= 95){
            nilaikredit = 1;
        } else if (ratio > 95 && ratio <= 97){
            nilaikredit = 2;
        } else if ( ratio > 97 && ratio <= 99){
            nilaikredit = 3;
        } else if (ratio > 99){
            nilaikredit = 4;
        }

        var bobot = 1;
        var score =getscorefromnilai(nilaikredit);
        
        $("#hitung-asprototal").html(tabletext);
        $("#ratio-asprototal").html(ratio.toFixed(2) + '%');
        $("#nilai-asprototal").text(nilaikredit);
        $("#bobot-asprototal").text(bobot);
        $("#lastscore-asprototal").text(score);


        $("#hratio-asprototal").html(ratio.toFixed(2) + '%');
        $("#hnilai-asprototal").text(nilaikredit);
        $("#hskor-asprototal").text(score);
        $("#hkriteria-asprototal").text(cekkriteriasehat(score));

        var context = [];
        context.push(ratio.toFixed(2));
        context.push(nilaikredit);
        context.push(bobot);
        context.push(score);
        
        return context;
    }

    function calpinjasprod(){
        var title1= 'Pinjaman Diberikan';
        var title2= 'Total Aset Produktif';
        var value1 = $("input[name='lpk_pnjmberi']").val();
        var value2 = $("input[name='lpk_asetprod']").val();
        var tabletext = gettabletext(title1, value1, title2, value2);

        var ratio = Math.ceil(value1/value2 * 100) ;
        var nilaikredit =0;
        if ( ratio <= 75 ){
            nilaikredit = 1;
        } else if ( ratio > 75 && ratio <= 85 ){
            nilaikredit = 2;
        } else if (ratio > 85 && ratio <= 95  ){
            nilaikredit = 3;
        } else if (ratio > 95){
            nilaikredit = 4;
        }
        
        var bobot = 1;
        var score =getscorefromnilai(nilaikredit);
        
        $("#hitung-pinjasprod").html(tabletext);
        $("#ratio-pinjasprod").html(ratio.toFixed(2) + '%');
        $("#nilai-pinjasprod").text(nilaikredit);
        $("#bobot-pinjasprod").text(bobot);
        $("#lastscore-pinjasprod").text(score);

        $("#hratio-pinjasprod").html(ratio.toFixed(2) + '%');
        $("#hnilai-pinjasprod").text(nilaikredit);
        $("#hskor-pinjasprod").text(score);
        $("#hkriteria-pinjasprod").text(cekkriteriasehat(score));

        var context = [];
        context.push(ratio.toFixed(2));
        context.push(nilaikredit);
        context.push(bobot);
        context.push(score);
        
        return context;
    }

    function calaliktotal(){
        var title1= 'Aset Likuid';
        var title2= 'Total Aset';
        var value1 = $("input[name='lpk_astliquid']").val();
        var value2 = $("input[name='lpk_totaset']").val();
        var tabletext = gettabletext(title1, value1, title2, value2);

        var ratio = Math.ceil(value1/value2 * 100) ;
        var nilaikredit =0;
        if ( ratio > 15 ){
            nilaikredit = 1;
        } else if ( ratio > 11 && ratio <= 15 ){
            nilaikredit = 2;
        } else if (ratio > 6 && ratio <= 10  ){
            nilaikredit = 3;
        } else if (ratio <= 5){
            nilaikredit = 4;
        }

        var bobot = 1;
        var score =getscorefromnilai(nilaikredit);
        
        $("#hitung-aliktotal").html(tabletext);
        $("#ratio-aliktotal").html(ratio.toFixed(2) + '%');
        $("#nilai-aliktotal").text(nilaikredit);
        $("#bobot-aliktotal").text(bobot);
        $("#lastscore-aliktotal").text(score);

        $("#hratio-aliktotal").html(ratio.toFixed(2) + '%');
        $("#hnilai-aliktotal").text(nilaikredit);
        $("#hskor-aliktotal").text(score);
        $("#hkriteria-aliktotal").text(cekkriteriasehat(score));

        var context = [];
        context.push(ratio.toFixed(2));
        context.push(nilaikredit);
        context.push(bobot);
        context.push(score);
        
        return context;
    }

    function calalikwajib(){
        var title1= 'Aset Likuid';
        var title2= 'Kewajiban Lancar';
        var value1 = $("input[name='lpk_astliquid']").val();
        var value2 = $("input[name='lpk_wjblncar']").val();
        var tabletext = gettabletext(title1, value1, title2, value2);

        var ratio = Math.ceil(value1/value2 * 100) ;
        var nilaikredit =0;
        if ( ratio > 21 ){
            nilaikredit = 1;
        } else if ( ratio > 15 && ratio <= 21 ){
            nilaikredit = 2;
        } else if (ratio > 8 && ratio <= 15  ){
            nilaikredit = 3;
        } else if (ratio <= 8){
            nilaikredit = 4;
        }

        var bobot = 1;
        var score =getscorefromnilai(nilaikredit);
        
        $("#hitung-alikwajib").html(tabletext);
        $("#ratio-alikwajib").html(ratio.toFixed(2) + '%');
        $("#nilai-alikwajib").text(nilaikredit);
        $("#bobot-alikwajib").text(bobot);
        $("#lastscore-alikwajib").text(score);

        $("#hratio-alikwajib").html(ratio.toFixed(2) + '%');
        $("#hnilai-alikwajib").text(nilaikredit);
        $("#hskor-alikwajib").text(score);
        $("#hkriteria-alikwajib").text(cekkriteriasehat(score));

        var context = [];
        context.push(ratio.toFixed(2));
        context.push(nilaikredit);
        context.push(bobot);
        context.push(score);
        
        return context;
    }

    function calrentaset(){
        var title1= 'SHU Setelah Pajak (EAT)';
        var title2= 'Total Aset';
        var value1 = $("input[name='lpk_shupjk']").val();
        var value2 = $("input[name='lpk_totaset']").val();
        var tabletext = gettabletext(title1, value1, title2, value2);

        var ratio = value1/value2 * 100;
        var nilaikredit =0;
        if (ratio < 3){
            nilaikredit = 4;
        } else if (ratio >= 3 && ratio < 5){
            nilaikredit = 3;
        } else if (ratio >= 5 && ratio < 7){
            nilaikredit = 2;
        } else if (ratio >= 7){
            nilaikredit = 1;
        }

        var bobot = 1;
        var score =getscorefromnilai(nilaikredit);
        
        $("#hitung-roa").html(tabletext);
        $("#ratio-roa").html(ratio.toFixed(2) + '%');
        $("#nilai-roa").text(nilaikredit);
        $("#bobot-roa").text(bobot);
        $("#lastscore-roa").text(score);

        $("#hratio-roa").html( ratio.toFixed(2) + '%');
        $("#hnilai-roa").text(nilaikredit);
        $("#hskor-roa").text(score);
        $("#hkriteria-roa").text(cekkriteriasehat(score));

        var context = [];
        context.push(ratio.toFixed(2));
        context.push(nilaikredit);
        context.push(bobot);
        context.push(score);
        
        return context;
    }

    function calrentekuitas(){
        var title1= 'SHU Setelah Pajak (EAT)';
        var title2= 'Total Modal Sendiri';
        var value1 = $("input[name='lpk_shupjk']").val();
        var value2 = $("input[name='lpk_totmdlsdr']").val();
        var tabletext = gettabletext(title1, value1, title2, value2);

        var ratio = value1/value2 * 100;
        var nilaikredit =0;
        if (ratio < 5){
            nilaikredit = 4;
        } else if (ratio >= 5 &&  ratio < 7.5){
            nilaikredit = 3;
        } else if (ratio >= 7.5 &&  ratio < 10){
            nilaikredit = 2;
        } else if (ratio >= 10){
            nilaikredit = 1;
        }

        var bobot = 1;
        var score =getscorefromnilai(nilaikredit);
        
        $("#hitung-roe").html(tabletext);
        $("#ratio-roe").html(ratio.toFixed(2) + '%');
        $("#nilai-roe").text(nilaikredit);
        $("#bobot-roe").text(bobot);
        $("#lastscore-roe").text(score);


        $("#hratio-roe").html(ratio.toFixed(2) + '%');
        $("#hnilai-roe").text(nilaikredit);
        $("#hskor-roe").text(score);
        $("#hkriteria-roe").text(cekkriteriasehat(score));

        var context = [];
        context.push(ratio.toFixed(2));
        context.push(nilaikredit);
        context.push(bobot);
        context.push(score);
        
        return context;
    }


    function calmandiriop(){
        var title1= 'Partisipasi Neto';
        var title2= 'Beban Usaha + Beban Perkop';
        var value1 = $("input[name='lpk_ptsneto']").val();
        var value2 = parseInt($("input[name='lpk_bbnusaha']").val()) +  parseInt($("input[name='lpk_bbnperkop']").val());
        var tabletext = gettabletext(title1, value1, title2, value2);

        var ratio = value1/value2 * 100;
        var nilaikredit =0;
        if (ratio <= 100){
            nilaikredit = 4;
        } else if (ratio > 100 && ratio <= 110){
            nilaikredit = 3;
        } else if (ratio > 110 && ratio <= 120){
            nilaikredit = 2;
        } else if (ratio > 120){
            nilaikredit = 1;
        }

        var bobot = 1;
        var score =getscorefromnilai(nilaikredit);
        
        $("#hitung-kmo").html(tabletext);
        $("#ratio-kmo").html(ratio.toFixed(2) + '%');
        $("#nilai-kmo").text(nilaikredit);
        $("#bobot-kmo").text(bobot);
        $("#lastscore-kmo").text(score);


        $("#hratio-kmo").html(ratio.toFixed(2) + '%');
        $("#hnilai-kmo").text(nilaikredit);
        $("#hskor-kmo").text(score);
        $("#hkriteria-kmo").text(cekkriteriasehat(score));

        var context = [];
        context.push(ratio.toFixed(2));
        context.push(nilaikredit);
        context.push(bobot);
        context.push(score);
        
        return context;
    }

    function calbodanpo(){
        var title1= 'Biaya Operasional';
        var title2= 'Pendapatan Operasional';
        var value1 = $("input[name='lpk_biayaoper']").val();
        var value2 = $("input[name='lpk_pendoper']").val();
        var tabletext = gettabletext(title1, value1, title2, value2);

        var ratio = value1/value2 * 100;
        var nilaikredit =0;
        if (ratio >= 100){
            nilaikredit = 4;
        } else if (ratio < 100 && ratio >= 90){
            nilaikredit = 3;
        } else if (ratio < 90 && ratio >= 80){
            nilaikredit = 2;
        } else if (ratio < 80 && ratio >= 0){
            nilaikredit = 1;
        }

        var bobot = 1;
        var score =getscorefromnilai(nilaikredit);
        
        $("#hitung-bopo").html(tabletext);
        $("#ratio-bopo").html(ratio.toFixed(2) + '%');
        $("#nilai-bopo").text(nilaikredit);
        $("#bobot-bopo").text(bobot);
        $("#lastscore-bopo").text(score);


        $("#hratio-bopo").html(ratio.toFixed(2) + '%');
        $("#hnilai-bopo").text(nilaikredit);
        $("#hskor-bopo").text(score);
        $("#hkriteria-bopo").text(cekkriteriasehat(score));

        var context = [];
        context.push(ratio.toFixed(2));
        context.push(nilaikredit);
        context.push(bobot);
        context.push(score);
        
        return context;
    }


    function calbudanshuk(){
        var title1= 'Biaya Usaha';
        var title2= 'SHU Kotor';
        var value1 = $("input[name='lpk_bbnusaha']").val();
        var value2 = $("input[name='lpk_shukotor']").val();
        var tabletext = gettabletext(title1, value1, title2, value2);

        var ratio = value1/value2 * 100;
        var nilaikredit =0;
        if (ratio >= 80){
            nilaikredit = 4;
        } else if (ratio >= 60 && ratio < 80){
            nilaikredit = 3;
        } else if (ratio >= 40 && ratio < 60){
            nilaikredit = 2;
        } else if (ratio < 40){
            nilaikredit = 1;
        }

        var bobot = 1;
        var score =getscorefromnilai(nilaikredit);
        
        $("#hitung-busk").html(tabletext);
        $("#ratio-busk").html(ratio.toFixed(2) + '%');
        $("#nilai-busk").text(nilaikredit);
        $("#bobot-busk").text(bobot);
        $("#lastscore-busk").text(score);

        $("#hratio-busk").html(ratio.toFixed(2) + '%');
        $("#hnilai-busk").text(nilaikredit);
        $("#hskor-busk").text(score);
        $("#hkriteria-busk").text(cekkriteriasehat(score));

        var context = [];
        context.push(ratio.toFixed(2));
        context.push(nilaikredit);
        context.push(bobot);
        context.push(score);
        
        return context;
    }



    function calpdadantp(){
        var title1= 'Pinjaman pada Anggota ';
        var title2= 'Total Piutang';
        var value1 = $("input[name='lpk_pjmanggta']").val();
        var value2 = $("input[name='lpk_totpiutng']").val();
        var tabletext = gettabletext(title1, value1, title2, value2);

        var ratio = value1/value2 * 100;
        var nilaikredit =0;
        if (ratio < 25){
            nilaikredit = 4;
        } else if (ratio >= 25 && ratio < 50){
            nilaikredit = 3;
        } else if (ratio >= 50 && ratio < 75){
            nilaikredit = 2;
        } else if (ratio >= 75){
            nilaikredit = 1;
        }


        var bobot = 1;
        var score =getscorefromnilai(nilaikredit);
        
        $("#hitung-patp").html(tabletext);
        $("#ratio-patp").html(ratio.toFixed(2) + '%');
        $("#nilai-patp").text(nilaikredit);
        $("#bobot-patp").text(bobot);
        $("#lastscore-patp").text(score);

        $("#hratio-patp").html(ratio.toFixed(2) + '%');
        $("#hnilai-patp").text(nilaikredit);
        $("#hskor-patp").text(score);
        $("#hkriteria-patp").text(cekkriteriasehat(score));

        var context = [];
        context.push(ratio.toFixed(2));
        context.push(nilaikredit);
        context.push(bobot);
        context.push(score);
        
        return context;
    }

    function calpbmdantp(){
        var title1= 'Pinjaman Bermasalah ';
        var title2= 'Total Piutang';
        var value1 = $("input[name='lpk_pjmbmslh']").val();
        var value2 = $("input[name='lpk_totpiutng']").val();
        var tabletext = gettabletext(title1, value1, title2, value2);

        var ratio = value1/value2 * 100;
        var nilaikredit =0;
        if (ratio > 15){
            nilaikredit = 4;
        } else if (ratio > 10 && ratio <= 15){
            nilaikredit = 3;
        } else if (ratio > 5 && ratio <= 10){
            nilaikredit = 2;
        } else if (ratio <=5 ){
            nilaikredit = 1;
        }


        var bobot = 1;
        var score =getscorefromnilai(nilaikredit);
        
        $("#hitung-pbtp").html(tabletext);
        $("#ratio-pbtp").html(ratio.toFixed(2) + '%');
        $("#nilai-pbtp").text(nilaikredit);
        $("#bobot-pbtp").text(bobot);
        $("#lastscore-pbtp").text(score);

        $("#hratio-pbtp").html(ratio.toFixed(2) + '%');
        $("#hnilai-pbtp").text(nilaikredit);
        $("#hskor-pbtp").text(score);
        $("#hkriteria-pbtp").text(cekkriteriasehat(score));

        var context = [];
        context.push(ratio.toFixed(2));
        context.push(nilaikredit);
        context.push(bobot);
        context.push(score);
        
        return context;
    }

    function calcdrsisk(){
        var title1= 'Cadangan Risiko ';
        var title2= 'Pinjaman Bermasalah';
        var value1 = $("input[name='lpk_cadrisk']").val();
        var value2 = $("input[name='lpk_pjmbmslh']").val();
        var tabletext = gettabletext(title1, value1, title2, value2);

        var ratio = value1/value2 * 100;
        var nilaikredit =0;
        if (ratio < 25){
            nilaikredit = 4;
        } else if (ratio >= 25 && ratio < 50){
            nilaikredit = 3;
        } else if (ratio >= 50 && ratio < 75){
            nilaikredit = 2;
        } else if (ratio >=75){
            nilaikredit = 1;
        }


        var bobot = 1;
        var score =getscorefromnilai(nilaikredit);
        
        $("#hitung-crpb").html(tabletext);
        $("#ratio-crpb").html(ratio.toFixed(2) + '%');
        $("#nilai-crpb").text(nilaikredit);
        $("#bobot-crpb").text(bobot);
        $("#lastscore-crpb").text(score);


        $("#hratio-crpb").html(ratio.toFixed(2) + '%');
        $("#hnilai-crpb").text(nilaikredit);
        $("#hskor-crpb").text(score);
        $("#hkriteria-crpb").text(cekkriteriasehat(score));

        var context = [];
        context.push(ratio.toFixed(2));
        context.push(nilaikredit);
        context.push(bobot);
        context.push(score);
        
        return context;
    }


    function calkasbankkjp(){
        var title1= 'Kas + Bank';
        var title2= 'Kewajiban Jangka Pendek';
        var value1 = $("input[name='lpk_kasbank']").val();
        var value2 = $("input[name='lpk_biayaoper']").val();
        var tabletext = gettabletext(title1, value1, title2, value2);

        var ratio = value1/value2 * 100;
        var nilaikredit =0;
        if (ratio < 10){
            nilaikredit = 4;
        } else if (ratio >= 10 && ratio < 15){
            nilaikredit = 3;
        } else if (ratio >= 15 && ratio < 20){
            nilaikredit = 2;
        } else if (ratio >=20){
            nilaikredit = 1;
        }


        var bobot = 1;
        var score =getscorefromnilai(nilaikredit);
        
        $("#hitung-kbwjp").html(tabletext);
        $("#ratio-kbwjp").html(ratio.toFixed(2) + '%');
        $("#nilai-kbwjp").text(nilaikredit);
        $("#bobot-kbwjp").text(bobot);
        $("#lastscore-kbwjp").text(score);

        $("#hratio-kbwjp").html(ratio.toFixed(2) + '%');
        $("#hnilai-kbwjp").text(nilaikredit);
        $("#hskor-kbwjp").text(score);
        $("#hkriteria-kbwjp").text(cekkriteriasehat(score));

        var context = [];
        context.push(ratio.toFixed(2));
        context.push(nilaikredit);
        context.push(bobot);
        context.push(score);
        
        return context;
    }


    function calpiutangdanaterima(){
        var title1= 'Piutang';
        var title2= 'Dana Yang Diterima';
        var value1 = $("input[name='lpk_totpiutng']").val();
        var value2 = $("input[name='lpk_danain']").val();
        var tabletext = gettabletext(title1, value1, title2, value2);

        var ratio = value1/value2 * 100;
        var nilaikredit =0;
        if (ratio < 60){
            nilaikredit = 4;
        } else if (ratio >= 60 && ratio < 75){
            nilaikredit = 3;
        } else if (ratio >= 75 && ratio < 90){
            nilaikredit = 2;
        } else if (ratio >= 90){
            nilaikredit = 1;
        }


        var bobot = 1;
        var score =getscorefromnilai(nilaikredit);
        
        $("#hitung-pdd").html(tabletext);
        $("#ratio-pdd").html(ratio.toFixed(2) + '%');
        $("#nilai-pdd").text(nilaikredit);
        $("#bobot-pdd").text(bobot);
        $("#lastscore-pdd").text(score);

        $("#hratio-pdd").html(ratio.toFixed(2) + '%');
        $("#hnilai-pdd").text(nilaikredit);
        $("#hskor-pdd").text(score);
        $("#hkriteria-pdd").text(cekkriteriasehat(score));

        var context = [];
        context.push(ratio.toFixed(2));
        context.push(nilaikredit);
        context.push(bobot);
        context.push(score);
        
        return context;
    }

    function calasetlancarwajibjp(){
        var title1= 'Aset Lancar';
        var title2= 'Kewajiban Jk. Pendek';
        var value1 = $("input[name='lpk_asetlancr']").val();
        var value2 = $("input[name='lpk_biayaoper']").val();
        var tabletext = gettabletext(title1, value1, title2, value2);

        var ratio = value1/value2 * 100;
        var nilaikredit =0;
        if (ratio < 75){
            nilaikredit = 4;
        } else if (ratio >= 75 && ratio < 100){
            nilaikredit = 3;
        } else if (ratio >= 100 && ratio < 125){
            nilaikredit = 2;
        } else if (ratio >= 125){
            nilaikredit = 1;
        }


        var bobot = 1;
        var score =getscorefromnilai(nilaikredit);
        
        $("#hitung-alwjp").html(tabletext);
        $("#ratio-alwjp").html(ratio.toFixed(2) + '%');
        $("#nilai-alwjp").text(nilaikredit);
        $("#bobot-alwjp").text(bobot);
        $("#lastscore-alwjp").text(score);

        $("#hratio-alwjp").html(ratio.toFixed(2) + '%');
        $("#hnilai-alwjp").text(nilaikredit);
        $("#hskor-alwjp").text(score);
        $("#hkriteria-alwjp").text(cekkriteriasehat(score));

        var context = [];
        context.push(ratio.toFixed(2));
        context.push(nilaikredit);
        context.push(bobot);
        context.push(score);
        
        return context;
    }

    function caltumbuhaset(){
        var title1= 'Aset Tahun Berjalan';
        var title2= 'Aset Tahun Lalu';
        var value1 = $("input[name='lpk_totaset']").val();
        var value2 = $("input[name='lpk_asetthnlalu']").val();
        var tabletext = gettabletext(title1, value1, title2, value2);

        var ratio = value1/value2 * 100;
        var nilaikredit =0;
        if (ratio < 4){
            nilaikredit = 4;
        } else if (ratio >= 4 && ratio < 7){
            nilaikredit = 3;
        } else if (ratio >= 7 && ratio < 10){
            nilaikredit = 2;
        } else if (ratio >= 10){
            nilaikredit = 1;
        }


        var bobot = 1;
        var score =getscorefromnilai(nilaikredit);
        
        $("#hitung-ptas").html(tabletext);
        $("#ratio-ptas").html(ratio.toFixed(2) + '%');
        $("#nilai-ptas").text(nilaikredit);
        $("#bobot-ptas").text(bobot);
        $("#lastscore-ptas").text(score);

        $("#hratio-ptas").html(ratio.toFixed(2) + '%');
        $("#hnilai-ptas").text(nilaikredit);
        $("#hskor-ptas").text(score);
        $("#hkriteria-ptas").text(cekkriteriasehat(score));

        var context = [];
        context.push(ratio.toFixed(2));
        context.push(nilaikredit);
        context.push(bobot);
        context.push(score);
        
        return context;
    }

    function caltumbuhdanaditerima(){
        var title1= 'Dana Diterima Tahun Berjalan';
        var title2= 'Dana Diterima Tahun Lalu';
        var value1 = $("input[name='lpk_danain']").val();
        var value2 = $("input[name='lpk_dninthnlalu']").val();
        var tabletext = gettabletext(title1, value1, title2, value2);

        var ratio = value1/value2 * 100;
        var nilaikredit =0;
        if (ratio < 4){
            nilaikredit = 4;
        } else if (ratio >= 4 && ratio < 7){
            nilaikredit = 3;
        } else if (ratio >= 7 && ratio < 10){
            nilaikredit = 2;
        } else if (ratio >= 10){
            nilaikredit = 1;
        }


        var bobot = 1;
        var score =getscorefromnilai(nilaikredit);
        
        $("#hitung-ptdd").html(tabletext);
        $("#ratio-ptdd").html(ratio.toFixed(2) + '%');
        $("#nilai-ptdd").text(nilaikredit);
        $("#bobot-ptdd").text(bobot);
        $("#lastscore-ptdd").text(score);

        $("#hratio-ptdd").html(ratio.toFixed(2) + '%');
        $("#hnilai-ptdd").text(nilaikredit);
        $("#hskor-ptdd").text(score);
        $("#hkriteria-ptdd").text(cekkriteriasehat(score));

        var context = [];
        context.push(ratio.toFixed(2));
        context.push(nilaikredit);
        context.push(bobot);
        context.push(score);
        
        return context;
    }

    function caltumbuhekuitas(){
        var title1= 'Modal Sendiri Tahun Berjalan';
        var title2= 'Modal Sendiri Tahun Lalu';
        var value1 = $("input[name='lpk_totmdlsdr']").val();
        var value2 = $("input[name='lpk_modalthnlalu']").val();
        var tabletext = gettabletext(title1, value1, title2, value2);

        var ratio = value1/value2 * 100;
        var nilaikredit =0;
        if (ratio < 4){
            nilaikredit = 4;
        } else if (ratio >= 4 && ratio < 7){
            nilaikredit = 3;
        } else if (ratio >= 7 && ratio < 10){
            nilaikredit = 2;
        } else if (ratio >= 10){
            nilaikredit = 1;
        }


        var bobot = 1;
        var score =getscorefromnilai(nilaikredit);
        
        $("#hitung-ptek").html(tabletext);
        $("#ratio-ptek").html(ratio.toFixed(2) + '%');
        $("#nilai-ptek").text(nilaikredit);
        $("#bobot-ptek").text(bobot);
        $("#lastscore-ptek").text(score);

        $("#hratio-ptek").html(ratio.toFixed(2) + '%');
        $("#hnilai-ptek").text(nilaikredit);
        $("#hskor-ptek").text(score);
        $("#hkriteria-ptek").text(cekkriteriasehat(score));

        var context = [];
        context.push(ratio.toFixed(2));
        context.push(nilaikredit);
        context.push(bobot);
        context.push(score);
        
        return context;
    }


    function caltumbuhhasilusahabersih(){
        var title1= 'Hasil Usaha Tahun Berjalan';
        var title2= 'Hasil Usaha Tahun Lalu';
        var value1 = $("input[name='lpk_shupjk']").val();
        var value2 = $("input[name='lpk_hasilthnlalu']").val();
        var tabletext = gettabletext(title1, value1, title2, value2);

        var ratio = value1/value2 * 100;
        var nilaikredit =0;
        if (ratio < 1){
            nilaikredit = 4;
        } else if (ratio >= 1 && ratio < 3){
            nilaikredit = 3;
        } else if (ratio >= 3 && ratio < 5){
            nilaikredit = 2;
        } else if (ratio >= 5){
            nilaikredit = 1;
        }


        var bobot = 1;
        var score =getscorefromnilai(nilaikredit);
        
        $("#hitung-ptub").html(tabletext);
        $("#ratio-ptub").html(ratio.toFixed(2) + '%');
        $("#nilai-ptub").text(nilaikredit);
        $("#bobot-ptub").text(bobot);
        $("#lastscore-ptub").text(score);


        $("#hratio-ptub").html(ratio.toFixed(2) + '%');
        $("#hnilai-ptub").text(nilaikredit);
        $("#hskor-ptub").text(score);
        $("#hkriteria-ptub").text(cekkriteriasehat(score));

        var context = [];
        context.push(ratio.toFixed(2));
        context.push(nilaikredit);
        context.push(bobot);
        context.push(score);
        
        return context;
    }

    function calpdptutamatotalpdpt(){
        var title1= 'Pendapatan Utama';
        var title2= 'Total Pendapatan';
        var value1 = $("input[name='lpk_pendutama']").val();
        var value2 = $("input[name='lpk_totalpendt']").val();
        var tabletext = gettabletext(title1, value1, title2, value2);

        var ratio = value1/value2 * 100;
        var nilaikredit =0;
        if (ratio < 35){
            nilaikredit = 4;
        } else if (ratio >= 35 && ratio < 60){
            nilaikredit = 3;
        } else if (ratio >= 60 && ratio < 85){
            nilaikredit = 2;
        } else if (ratio >= 85){
            nilaikredit = 1;
        }


        var bobot = 1;
        var score =getscorefromnilai(nilaikredit);
        
        $("#hitung-putp").html(tabletext);
        $("#ratio-putp").html(ratio.toFixed(2) + '%');
        $("#nilai-putp").text(nilaikredit);
        $("#bobot-putp").text(bobot);
        $("#lastscore-putp").text(score);

        $("#hratio-putp").html(ratio.toFixed(2) + '%');
        $("#hnilai-putp").text(nilaikredit);
        $("#hskor-putp").text(score);
        $("#hkriteria-putp").text(cekkriteriasehat(score));

        var context = [];
        context.push(ratio.toFixed(2));
        context.push(nilaikredit);
        context.push(bobot);
        context.push(score);
        
        return context;
    }


    function calshbersihsps(){
        var title1= 'SHU Bersih';
        var title2= 'Simp. Pokok + Simp. Wajib';
        var value1 = $("input[name='lpk_shupjk']").val();
        var value2 = parseInt($("input[name='lpk_simppokok']").val())+ parseInt($("input[name='lpk_simpwajib']").val());
        var tabletext = gettabletext(title1, value1, title2, value2);

        var ratio = value1/value2 * 100;
        var nilaikredit =0;
        if (ratio < 10){
            nilaikredit = 4;
        } else if (ratio >= 10 && ratio < 20){
            nilaikredit = 3;
        } else if (ratio >= 20 && ratio < 30){
            nilaikredit = 2;
        } else if (ratio >= 30){
            nilaikredit = 1;
        }


        var bobot = 1;
        var score =getscorefromnilai(nilaikredit);
        
        $("#hitung-sbsps").html(tabletext);
        $("#ratio-sbsps").html(ratio.toFixed(2) + '%');
        $("#nilai-sbsps").text(nilaikredit);
        $("#bobot-sbsps").text(bobot);
        $("#lastscore-sbsps").text(score);

        $("#hratio-sbsps").html(ratio.toFixed(2) + '%');
        $("#hnilai-sbsps").text(nilaikredit);
        $("#hskor-sbsps").text(score);
        $("#hkriteria-sbsps").text(cekkriteriasehat(score));

        var context = [];
        context.push(ratio.toFixed(2));
        context.push(nilaikredit);
        context.push(bobot);
        context.push(score);
        
        return context;
    }

    function calpartisipasisimagt(){
        var title1= 'Simpanan Anggota Yang Masuk';
        var title2= 'Total Simpanan Yang Masuk';
        var value1 = $("input[name='lpk_simpanggtin']").val();
        var value2 = $("input[name='lpk_totalsimpin']").val();
        var tabletext = gettabletext(title1, value1, title2, value2);

        var ratio = value1/value2 * 100;
        var nilaikredit =0;
        if (ratio < 25){
            nilaikredit = 4;
        } else if (ratio >= 25 && ratio < 50){
            nilaikredit = 3;
        } else if (ratio >= 50 && ratio < 75){
            nilaikredit = 2;
        } else if (ratio >= 75){
            nilaikredit = 1;
        }


        var bobot = 1;
        var score =getscorefromnilai(nilaikredit);
        
        $("#hitung-psa").html(tabletext);
        $("#ratio-psa").html(ratio.toFixed(2) + '%');
        $("#nilai-psa").text(nilaikredit);
        $("#bobot-psa").text(bobot);
        $("#lastscore-psa").text(score);

        $("#hratio-psa").html(ratio.toFixed(2) + '%');
        $("#hnilai-psa").text(nilaikredit);
        $("#hskor-psa").text(score);
        $("#hkriteria-psa").text(cekkriteriasehat(score));

        var context = [];
        context.push(ratio.toFixed(2));
        context.push(nilaikredit);
        context.push(bobot);
        context.push(score);
        
        return context;
    }

    function calekuitastotalaset(){
        var title1= 'Modal Sendiri';
        var title2= 'Total Aset';
        var value1 = $("input[name='lpk_totmdlsdr']").val();
        var value2 = $("input[name='lpk_totaset']").val();
        var tabletext = gettabletext(title1, value1, title2, value2);

        var ratio = value1/value2 * 100;
        var nilaikredit =0;
        if (ratio < 10){
            nilaikredit = 4;
        } else if (ratio >= 10 && ratio < 20){
            nilaikredit = 3;
        } else if (ratio >= 20 && ratio < 30){
            nilaikredit = 2;
        } else if (ratio >= 30){
            nilaikredit = 1;
        }


        var bobot = 1;
        var score =getscorefromnilai(nilaikredit);
        
        $("#hitung-eta").html(tabletext);
        $("#ratio-eta").html(ratio.toFixed(2) + '%');
        $("#nilai-eta").text(nilaikredit);
        $("#bobot-eta").text(bobot);
        $("#lastscore-eta").text(score);

        $("#hratio-eta").html(ratio.toFixed(2) + '%');
        $("#hnilai-eta").text(nilaikredit);
        $("#hskor-eta").text(score);
        $("#hkriteria-eta").text(cekkriteriasehat(score));

        var context = [];
        context.push(ratio.toFixed(2));
        context.push(nilaikredit);
        context.push(bobot);
        context.push(score);
        
        return context;
    }

    function calcukupmodal(){
        var title1= 'Modal Tertimbang';
        var title2= 'ATMR';
        var value1 = $("input[name='lpk_modtimbang']").val();
        var value2 = $("input[name='lpk_atmr']").val();
        var tabletext = gettabletext(title1, value1, title2, value2);

        var ratio = value1/value2 * 100;
        var nilaikredit =0;
        if (ratio < 4){
            nilaikredit = 4;
        } else if (ratio >= 4 && ratio < 6){
            nilaikredit = 3;
        } else if (ratio >= 6 && ratio < 8){
            nilaikredit = 2;
        } else if (ratio >= 8){
            nilaikredit = 1;
        }


        var bobot = 1;
        var score =getscorefromnilai(nilaikredit);
        
        $("#hitung-kcm").html(tabletext);
        $("#ratio-kcm").html(ratio.toFixed(2) + '%');
        $("#nilai-kcm").text(nilaikredit);
        $("#bobot-kcm").text(bobot);
        $("#lastscore-kcm").text(score);

        $("#hratio-kcm").html(ratio.toFixed(2) + '%');
        $("#hnilai-kcm").text(nilaikredit);
        $("#hskor-kcm").text(score);
        $("#hkriteria-kcm").text(cekkriteriasehat(score));

        var context = [];
        context.push(ratio.toFixed(2));
        context.push(nilaikredit);
        context.push(bobot);
        context.push(score);
        
        return context;
    }

    function calmodalpinjamaset(){
        var title1= 'Modal Pinjaman Anggota';
        var title2= 'Total Aset';
        var value1 = $("input[name='lpk_modpinjanggt']").val();
        var value2 = $("input[name='lpk_totaset']").val();
        var tabletext = gettabletext(title1, value1, title2, value2);

        var ratio = value1/value2 * 100;
        var nilaikredit =0;
        if (ratio < 10){
            nilaikredit = 4;
        } else if (ratio >= 10 && ratio < 20){
            nilaikredit = 3;
        } else if (ratio >= 20 && ratio < 30){
            nilaikredit = 2;
        } else if (ratio >= 30){
            nilaikredit = 1;
        }
        //lpk_totaset

        var bobot = 1;
        var score =getscorefromnilai(nilaikredit);
        
        $("#hitung-mpata").html(tabletext);
        $("#ratio-mpata").html(ratio.toFixed(2) + '%');
        $("#nilai-mpata").text(nilaikredit);
        $("#bobot-mpata").text(bobot);
        $("#lastscore-mpata").text(score);

        $("#hratio-mpata").html(ratio.toFixed(2) + '%');
        $("#hnilai-mpata").text(nilaikredit);
        $("#hskor-mpata").text(score);
        $("#hkriteria-mpata").text(cekkriteriasehat(score));

        var context = [];
        context.push(ratio.toFixed(2));
        context.push(nilaikredit);
        context.push(bobot);
        context.push(score);
        
        return context;
    }
    function calwjbjkpekuitas(){
        var title1= 'Kewajiban JK. Panjang';
        var title2= 'Ekuitas';
        var value1 = $("input[name='lpk_wjbjngkapjg']").val();
        var value2 = $("input[name='lpk_totmdlsdr']").val();
        var tabletext = gettabletext(title1, value1, title2, value2);

        var ratio = value1/value2 * 100;
        var nilaikredit =0;
        if (ratio > 150){
            nilaikredit = 4;
        } else if (ratio > 125 && ratio <= 150){
            nilaikredit = 3;
        } else if (ratio > 100 && ratio <= 125){
            nilaikredit = 2;
        } else if (ratio <= 100){
            nilaikredit = 1;
        }

        var bobot = 1;
        var score =getscorefromnilai(nilaikredit);
        
        $("#hitung-wjpe").html(tabletext);
        $("#ratio-wjpe").html(ratio.toFixed(2) + '%');
        $("#nilai-wjpe").text(nilaikredit);
        $("#bobot-wjpe").text(bobot);
        $("#lastscore-wjpe").text(score);

        $("#hratio-wjpe").html(ratio.toFixed(2) + '%');
        $("#hnilai-wjpe").text(nilaikredit);
        $("#hskor-wjpe").text(score);
        $("#hkriteria-wjpe").text(cekkriteriasehat(score));

        var context = [];
        context.push(ratio.toFixed(2));
        context.push(nilaikredit);
        context.push(bobot);
        context.push(score);
        
        return context;
    }

    function gettabletext(title1, value1, title2, value2){


        var text =
        "<table class='table table-borderless  table-sm  '>"+
            "<tbody>"+
                "<tr>"+
                    "<td class='text-center small'>"+ title1 +"</td>"+
                    "<td class='text-center'></td>"+
                    "<td class='text-center'></td>"+
                "</tr>"+
                "<tr>"+
                    "<td class='text-center small border-bottom border-3 border-dark'>"+value1+"</td>"+
                    "<td class='text-center small'>X</td>"+
                    "<td class='text-center small'>100%</td>"+
               " </tr>"+
                "<tr>"+
                    "<td class='text-center small'>"+ title2 +"</td>"+
                    "<td class='text-center'></td>"+
                    "<td class='text-center'></td>"+
                "</tr>"+
                "<tr>"+
                    "<td class='text-center small'>"+ value2 +"</td>"+
                    "<td class='text-center'></td>"+
                    "<td class='text-center'></td>"+
                "</tr>"+
            "</tbody>"+
        "</table>";

        return text;
    }

    function getscorefromnilai(nilai){
        var score = 0;
        if (nilai == 4){
            score = 1;
        } else if (nilai == 3){
            score = 2;
        } else if (nilai == 2){
            score = 3;
        } else if (nilai == 1){
            score = 4;
        }

        return score;
    }
    function getnilaifromratio(ratio){
        var nilaikredit = 0;
        if (ratio <= 25){
            nilaikredit = 4;
        } else if (ratio <= 50){
            nilaikredit = 3;
        } else if (ratio <= 75){
            nilaikredit = 2;
        } else if (ratio <= 100){
            nilaikredit = 1;
        }
        return nilaikredit;
    }