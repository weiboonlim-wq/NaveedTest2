const fs = require('fs');
const path = './static/index.html';
let html = fs.readFileSync(path, 'utf8');

// Replace embedded Lucide and XLSX with CDN links to reduce file size
const lucideCDN = '<script src="https://unpkg.com/lucide@latest"></script>';
const xlsxCDN = '<script src="https://cdnjs.cloudflare.com/ajax/libs/xlsx/0.18.5/xlsx.full.min.js"></script>';

// Find the start and end of the huge script blocks
// We look for the common SheetJS and Lucide header comments
const xlsxStart = html.indexOf('<script>/*! xlsx.js');
const xlsxEnd = html.indexOf('</script>', xlsxStart) + 9;

if (xlsxStart > -1) {
    html = html.substring(0, xlsxStart) + xlsxCDN + html.substring(xlsxEnd);
}

const lucideStart = html.indexOf('<script>/**\n * @license lucide');
const lucideEnd = html.indexOf('</script>', lucideStart) + 9;

if (lucideStart > -1) {
    html = html.substring(0, lucideStart) + lucideCDN + html.substring(lucideEnd);
}

fs.writeFileSync(path, html);
