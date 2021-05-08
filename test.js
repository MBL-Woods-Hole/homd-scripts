const path = require('path');
const fs = require('fs-extra');
file = 'homdData-TaxonLookup.json'
data = fs.readFileSync(file);
p = JSON.parse(data)
console.log(p)
