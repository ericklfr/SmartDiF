var onetime;
var img;
var fr;
var click = true;
var canvas2;
var ctx2;
var points = [];
var escalaX;
var escalaY;
var canvas;
var ctx;
var faces = [];
var ligado = false;
var chave=false;
var contador=0;
var canvasId = 'mostrarCanvas';
var input;
var files;
var faces_positions = [];
var minX,minY,maxX,maxY;
var borda;
var urlResultado;
var urlDragImg;
var urlIICimgLoad;
var urlGGEimgLoad;
var urlIICimg;
var urlGGEimg;

function getUrlsFromTemplate(urlResultado,urlDragImg,urlIICimgLoad,urlGGEimgLoad,urlIICimg,urlGGEimg){
	this.urlResultado = urlResultado;
	this.urlDragImg = urlDragImg;
	this.urlIICimgLoad = urlIICimgLoad;
	this.urlGGEimgLoad = urlGGEimgLoad;
	this.urlIICimg = urlIICimg;
	this.urlGGEimg = urlGGEimg;
}

function gerarDados(data){
	var dataBarsNormal = [];
	var dataBarsFake = [];
	for (tipo in data['resultado']){
	    if(tipo != "resultadoFinal"){
	        var contentNormal = " ";
	        var contentFake = " ";
	        var total = 0;
	        var porcentNormal = 0; 
	        var porcentFake = 0;
	        for (key in data['resultado'][tipo]) {
	            if(data['resultado'][tipo]['normal']!=0 || data['resultado'][tipo]['fake']!=0){
	                var total = data['resultado'][tipo]['normal'] + data['resultado'][tipo]['fake']
	                var porcentNormal = (data['resultado'][tipo]['normal']*100)/total 
	                var porcentFake = (data['resultado'][tipo]['fake']*100)/total
	                if(key != "normal" && key != "fake"){
	                    if(data['resultado'][tipo][key]['normal'] != 0){
	                    contentNormal += "<div align='center' ><strong>"+key.toUpperCase()+"</strong></div><strong><span style=\"color:green;margin-top:0px;font-family:roboto;\"> VOTOS:"+ data['resultado'][tipo][key]['normal']+"</span></strong>";
	                    }
	                    if (data['resultado'][tipo][key]['fake'] != 0){
	                    contentFake += "<div align='center' ><strong>"+key.toUpperCase()+ "</strong></div><strong><span style=\"color:red;margin-top:0px;font-family:roboto;\"> VOTOS:"+ data['resultado'][tipo][key]['fake']+"</span></strong>";
	                    }
	                }
	            }
	        }
	        if(total!=0){
	        dataBarsFake.push({y: porcentFake,label:tipo.toUpperCase(),toolTipContent:contentFake})
	        dataBarsNormal.push({y:porcentNormal,label:tipo.toUpperCase(),toolTipContent:contentNormal})
	    	}
	   	}   
	}
 return criarGrafico(dataBarsFake,dataBarsNormal)  
}

function criarGrafico(dataBarsFake,dataBarsNormal){
	var chart = new CanvasJS.Chart("chartContainer", {
    animationEnabled: true,
    title:{
        text: "Resultado dos Extratores",
        fontWeight: "bold",
    },
    axisX: {
        name: "Fake",
        labelFontWeight: "bold",
    },
    axisY: {

        prefix: "%",
        
    },
    toolTip: {
        shared: false,
        borderColor: "black",
    },
    legend:{
        cursor: "pointer",
        fontSize: 15,
        fontStyle: "bold",
    },

    data: [{
        type: "stackedBar100",
        name: "Fake",
        color: "#ff3737",
        showInLegend: "true",
        indexLabel: "#percent%",
        percentFormatString: "#0.##",
        yValueFormatString: "#0,##%",
          dataPoints: dataBarsFake
    },
    
    {
        type: "stackedBar100",
        name: "Normal",
        color: "#4bc70c",
        showInLegend: "true",
        indexLabel: "#percent%",
        percentFormatString: "#0.##",
        yValueFormatString: "#0,##%",
            
          dataPoints: dataBarsNormal
    }]
    }); 
	return chart    
}



function documentReady(){
    $('#submeter').on('click', function(){
	    
		var dialog = bootbox.dialog({
		
		message: '<p style="font-size:2em" ><i class="fa fa-spin fa-spinner fa-lg"></i> Analisando imagem...</p>',
		closeButton: false,
		onEscape: true,
		backdrop: true,
		size : 'modal2'

		});

		$(document).on('click', '.modal-backdrop', function (event) {
		bootbox.hideAll()
		});
		
			
	    var descritores = $("input[name=descritores]:checked").map(
	    function () {return this.value;}).get().join(" ");

	    var classificador = $("input[name=classificadores]:checked").map(
	    function () {return this.value;}).get().join(",");

	    var data = {'descritores':descritores,'faces_positions':faces_positions,'classificador':classificador}

	    $.ajax({
			url: urlResultado,
			type: "POST",
			contentType: 'application/json; charset=utf-8',
			data: JSON.stringify(data),
			dataType: 'json',
			success: function(data) {

				if(data['resultado']['resultadoFinal'] == 'FAKE'){
			    dialog.find('.bootbox-body').html('<h1 style="margin-top: 1em;text-align:center;vertical-align: middle">Classificação: <span  id = "classificacao" class="badge badge-danger"></span></h1> <div id="chartContainer" style="height: 300px; width: 100%;"></div>'
			    	);
			    }else{
					dialog.find('.bootbox-body').html('<h1 style="margin-top: 1em;text-align:center;vertical-align: middle">Classificação: <span id = "classificacao" class="badge badge-success"></span></h1> <div id="chartContainer" style="height: 300px; width: 100%;"></div>'
			    	);
			    }
			    var chart = gerarDados(data)
			    chart.render();
			    document.getElementById("classificacao").innerHTML = data['resultado']['resultadoFinal']
			},
		});
	});
}

function loadIICandGGE(){
	var fileInput = document.getElementById('file');
	var filename = fileInput.files[0].name;
	var parts = filename.split(".")
	var name = parts[0]+"_fhs.png"
	var div_iic = document.getElementById('iic');
	var div_gge = document.getElementById('gge');
	div_iic.style.display = "none";
	div_gge.style.display = "none";
	var loading_iic = document.getElementById('loading_iic');
	var loading_gge = document.getElementById('loading_gge');
	loading_iic.style.display = "initial";
	loading_gge.style.display = "initial";
	name = name.replace(/[\s()]/g,"_")
	var iic = new Image();
	var gge = new Image();
	iic.src =  urlIICimg+name;
	gge.src = urlGGEimg+name;

	iic.onerror = function() {
		setTimeout(loadIICandGGE(urlIICimg,urlGGEimg),10000);
	}
		gge.onerror = function() {
		setTimeout(loadIICandGGE(urlIICimg,urlGGEimg),10000);
	}

	iic.onload = function() { 
		document.getElementById('iic').src = iic.src
		div_iic.style.display = "initial"
		loading_iic.style.display = "none"
	}

	gge.onload = function() { 
		document.getElementById('gge').src = gge.src
		div_gge.style.display = "initial"
		loading_gge.style.display = "none"
	}
}

function limpar(){
	chave = false;

	for (var i = faces.length-1; i >= 0; i--) {
		faces[i]['canvas'].remove();
		faces.splice(i,1);
	}

	for (var j = faces_positions.length-1; j >= 0; j--){
		faces_positions.splice(j,1);
	}

	contador = 0;
	faces_positions = [];
	faces = [];
	document.getElementById("submeter").disabled = true;
	document.getElementById("file").value = "";
	var imgp = document.getElementById("imgp");
	imgp.style.border = "dashed white 2px";
	document.oncontextmenu = null;
	ligado = false;
	document.getElementById("file").disabled = false;
	document.getElementById("imgp").style.cursor = "pointer";
	canvas = document.getElementById("imgp");
	var loading_iic = document.getElementById('loading_iic');
	var loading_gge = document.getElementById('loading_gge');
	loading_iic.style.display = "none";
	loading_gge.style.display = "none";
	var div_iic = document.getElementById('iic');
	var div_gge = document.getElementById('gge');
	div_iic.style.display = "initial";
	div_gge.style.display = "initial";

	ctx.clearRect(0,0,ctx.canvas.width,ctx.canvas.height);

	img.src = urlDragImg;
	img.onload = function() {
		ctx.drawImage(img,0,0,ctx.canvas.width,ctx.canvas.height);
	};
	document.getElementById('iic').src = urlIICimgLoad;
	document.getElementById('gge').src = urlGGEimgLoad;
}

function windowOnload(){
	canvas = document.getElementById("imgp");
	borda =  document.getElementById('bordaPrincipal');
	canvas.style.cursor = "pointer";

	ctx = canvas.getContext('2d');
	ctx.canvas.width = borda.offsetWidth;
	ctx.canvas.height = borda.offsetHeight;
	img = new Image();
	img.src = urlDragImg;
	img.onload = function() {
	ctx.drawImage(img,0,0,ctx.canvas.width,ctx.canvas.height);
	};
	if(chave){
		ctx.clearRect(0,0,ctx.canvas.width, ctx.canvas.height);
		canvas.remove();
	}
}

function windowOnresize(){
    borda =  document.getElementById('bordaPrincipal');
    ctx.canvas.width = borda.offsetWidth;
    ctx.canvas.height = borda.offsetHeight;
    bg();
}

function loadImage() {
	onetime = false;
	if (!onetime){
		document.getElementById("form_img").submit();
		loadIICandGGE();
		document.getElementById("file").disabled = true;
		let dialog = bootbox.dialog({
		
		message: '<p style="font-size:1em;text-align:center" > Agora você precisa selecionar no mínimo duas faces, antes de submeter.</p>',
		closeButton: false,
		onEscape: true,
		backdrop: true,
		size : 'modal2'

		});
	}

	onetime = true;

	if (typeof window.FileReader !== 'function') {
	    write("The file API isn't supported on this browser yet.");
	    return;
	}

	input = document.getElementById('file');

	if (!input) {
	    write("Um, couldn't find the imgfile element.");
	} else if (!input.files) {
	    write("This browser doesn't seem to support the `files` property of file inputs.");
	} else if (!input.files[0]) {
	    write("Please select a file before clicking 'Load'");
	} else {
	    files = input.files[0];
	    fr = new FileReader();
	    fr.onloadend = function() {
		ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
		img.src = fr.result;
		imageLoaded();
		ligado = true;
	    }
	    fr.readAsDataURL(files);
	}
}

function imageLoaded() {
	ctx.drawImage(img,0,0,ctx.canvas.width,ctx.canvas.height);
	canvas.style.cursor = "crosshair";
	ctx.lineWidth = 2;
	ctx.strokeStyle = '#c00';
	ctx.lineCap = 'round';
	chave = true;
	imgp.style.border = "solid white 2px";

	canvas.onmousedown = function(e) {
		if(chave){
			if (e.button == 0){
				click = true;
				var pos = getXY(e);
				last = pos;
				points = [];
				isDown = true;
				points.push(pos);
				if (ligado){
					bg();
				}
			}else{
				if (ligado){
					bg();
				}
				canvas2.remove();
			}
		}
	};

	document.oncontextmenu = function(e){
		if (e.target.id=="imgp")
			return false
}

    canvas.onmousemove = function(e) {
        if (chave && click){
            if (!isDown) return;

            var pos = getXY(e);
            points.push(pos);
            ctx.beginPath();
            ctx.moveTo(last.x, last.y);
            ctx.lineTo(pos.x, pos.y);
            ctx.stroke();
            last = pos;

        }
    };


    canvas.onmouseup = function(e) {
        click = false;
        if(chave && points.length >= 4){
        click = true;

            if (ligado){
            bg();
            }

            if (!isDown) return;

            isDown = false;

            minMax();


            if (ligado){
            bg();
             }
            contador += 1;

            ctx.lineWidth = 2;
            ctx.strokeRect(minX, minY, maxX - minX, maxY - minY);
            var index = faces_positions.push({'minX':minX*escalaX,'minY':minY*escalaY,'maxX':maxX*escalaX,'maxY':maxY*escalaY}) -1;
            canvas2 = document.createElement('canvas');
            ctx2 = canvas2.getContext('2d');
            canvas2.id = ("face "+contador);
            canvas2.width  = 60;
            canvas2.height = 60;
            canvas2.style.position = "relative";
            canvas2.style.marginRight = "0px";
            canvas2.style.marginLeft = "15px";
            canvas2.style.marginBottom = "0px";
            canvas2.style.marginTop = "0px";
            canvas2.style.border   = "2px solid #666666";
            canvas2.style.borderRadius = "10px";
            var canvasPos = canvas2.getBoundingClientRect();

            canvas2.onmouseover = function(){
             this.style.border = "2px solid red";
             this.style.cursor = "pointer";
             }

            canvas2.onmouseout = function(){
            this.style.border = "2px solid #666666";
            }

            canvas2.onclick = function(){
                if (confirm("Deseja apagar a face selecionada?")){
                     for(var i=0; i<faces.length; i++){
                        if (faces[i]['id'] == this.id){
                            
                            faces_positions.splice(faces[i]['index'], 1);
                            faces.splice(faces.findIndex(x => x.id==this.id),1);
                            contador -= 1;
                        }
                    }
                
                if(faces.length<2){
                document.getElementById('submeter').disabled = true
                }
                this.faces = null;
                this.remove();
                }
            }

            ctx2.drawImage(img,minX*escalaX,minY*escalaY, maxX*escalaX - minX*escalaX, maxY*escalaY - minY*escalaY, 0, 0, 60, 60);
            var output = document.getElementById('mostrarCanvas');
            faces.push({'index':index,'id':canvas2.id,'canvas':canvas2});
            if(faces.length>=2){
                document.getElementById('submeter').disabled = false
            }
            output.innerHTML = '';
            for(var i=0; i<faces.length; i++){
            output.appendChild(faces[i]['canvas'])
                }
        }

    }
}
    


function bg(){
	ctx.drawImage(img,0,0,ctx.canvas.width,ctx.canvas.height);
}

function minMax() {
    escalaY = (img.height/canvas.height);
    escalaX = (img.width/canvas.width);
    var i = 0;
    var p;
    minX = 1000000;
    minY = 1000000;
    maxX = -1000000;
    maxY = -1000000;


    for(; p = points[i++];) {
        if (p.x > maxX) maxX = p.x;
        if (p.y > maxY) maxY = p.y;
        if (p.x < minX) minX = p.x;
        if (p.y < minY) minY = p.y;
    }
}



function getXY(e) {
var rect = canvas.getBoundingClientRect();
return {x: e.clientX - rect.left, y: e.clientY - rect.top}
}


function write(msg) {
    var p = document.createElement('p');
    p.innerHTML = msg;
    document.body.appendChild(p);
}
