var new_flat_count = 0
function Table_to_visible(){
  var table = document.getElementById("flat_table");
  if (table.style.visibility === 'hidden'){
    table.style.visibility= 'visible';
  }
  return table
}

function get_flat_template_clone(){
  return document.getElementById('flat_template').cloneNode(true)
}

function get_flats_data(){
  return JSON.parse(document.getElementsByName('flats_data')[0].value);
}

function parseChild(child_id,divs){
  var result = {}
  if (child_id){
    result['id'] = child_id
  }
  divs.forEach(function(div){
    var item = div.children[0]
    let key_name = div.id.split('_')[0]
    if (["entrance",'floor','language'].includes(key_name)){
      result[key_name] = parseInt(item.value||0)
    }else{
      if (key_name==='way'){key_name="way_desc"}
      result[key_name] = item.value||""
    }
  })
  return result
}

function update_flats_data(){
  let table = Table_to_visible()
  var flats = []
  let children = Array.from(table.children)
  children.forEach(function (child){
    // console.log(parseInt(child.id))
    if (child.id.search('template') === -1){
      let cur_id = child.id.split("_")[1]
      flats.push(parseChild(parseInt(cur_id),Array.from(child.children)))
    }
  })
  document.getElementsByName('flats_data')[0].value = JSON.stringify(flats)
}

function fillFlats(){
  const flats_data = get_flats_data();
  if (flats_data.length > 0) {
    let table = Table_to_visible()
    flats_data.forEach(function(flat){
      let row = addFlatRow(flat)
      table.appendChild(row)
    })
  }
}

function set_field_value(div, value){
  // const name = div.getAttribute('id')
  // div.children[0].setAttribute('id',name+id.toString())
  // div.children[0].setAttribute('name',name+id.toString())
  div.children[0].value = value
}
function addFlatRow(flat_dict){
  const clone = get_flat_template_clone();
  let f_id=flat_dict['id']||""
  clone.setAttribute('id', "flat_" + f_id)
  clone.style.visibility= 'visible';
  children = clone.children
    set_field_value(children[0],flat_dict['entrance']||"")
    set_field_value(children[1],flat_dict['number']||"")
    set_field_value(children[2],flat_dict['floor']||"")
    set_field_value(children[3],flat_dict['way_desc']||"")
    set_field_value(children[4],flat_dict['language']||1)
  return clone
}

function addRow () {
  var table = Table_to_visible()
  let clone = addFlatRow({})
  // "id": new_flat_count.toString()
  // })
  table.appendChild(clone)
}

