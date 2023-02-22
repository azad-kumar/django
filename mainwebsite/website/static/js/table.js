
mymessage=function()
{
  var myPythonList = ['item1', 'item2', 'item3'];
  var tablee=document.getElementById("myTable")
  var htmlCode = `
  <div class="table-row">
                    <div class="table-data">${myPythonList[0]}</div>
                    <div class="table-data">${myPythonList[1]}</div>
                    <div class="table-data">${myPythonList[2]}</div>
                </div>
  `;
  tablee.innerHTML += htmlCode;
}