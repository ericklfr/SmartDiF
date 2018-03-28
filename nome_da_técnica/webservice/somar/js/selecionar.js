var ctx = canvas.getContext('2d'),
    img = new Image;

ctx.lineWidth = 7;
ctx.strokeStyle = '#c00';
ctx.lineCap = 'round';

img.onload = start;
img.src = 'http://i.stack.imgur.com/2JweT.jpg';

function start() {
    
    var points = [],
        isDown = false,
        last;
    
    canvas.onmousedown = function(e) {
        var pos = getXY(e);
        last = pos;

        points = [];
        isDown = true;
        points.push(pos);

        bg();
    };

    canvas.onmousemove = function(e) {
    
        if (!isDown) return;
        
        var pos = getXY(e);
        points.push(pos);
        
        ctx.beginPath();
        ctx.moveTo(last.x, last.y);
        ctx.lineTo(pos.x, pos.y);
        ctx.stroke();
        
        last = pos;
    };

    canvas.onmouseup = function(e) {
        if (!isDown) return;
        
        isDown = false;
        
        minMax();
    };
    
    bg();

    function bg() {
        ctx.drawImage(img, 0, 0);
    }
    
    function minMax() {
        var minX = 1000000,
            minY = 1000000,
            maxX = -1000000,
            maxY = -1000000,
            i = 0, p,
            lw = ctx.lineWidth;
        
        for(; p = points[i++];) {
            if (p.x > maxX) maxX = p.x;
            if (p.y > maxY) maxY = p.y;
            if (p.x < minX) minX = p.x;
            if (p.y < minY) minY = p.y;
        }
        
        ctx.lineWidth = 3;
        ctx.strokeRect(minX, minY, maxX - minX, maxY - minY);
        ctx.lineWidth = lw;
    }
}


function getXY(e) {
    var rect = canvas.getBoundingClientRect();
    return {x: e.clientX - rect.left, y: e.clientY - rect.top}
}
