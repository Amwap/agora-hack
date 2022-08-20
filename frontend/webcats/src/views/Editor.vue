<template lang="">
  <div class='col-md-12 p-5 pt-3 d-flex align-items-start flex-column'>
    
    <h3>Editor</h3>
    <router-link class="" :to="'/'">
      <button class='btn btn-block btn-outline-secondary btn-sm'>&lt;- Back</button>
    </router-link> 
    <div class="col-md-12">
      <div class="col-md-2 toolbar mt-3"></div>
      <div class='col-md-12 workflow mt-3'>
        <ItemTree :item_list='canvas' @node-click="setCurrentItem"/>
      </div>
    </div>
  </div>
</template>
<script>
import ItemTree from "@/components/ItemTree.vue"

export default {
  components:{
    ItemTree
  },
  methods: {
    setCurrentItem(node) {
      console.log("Clicked: ", node.id);
      this.selected_item = node
    }
  },
  data() {
    return {
      selected_item: null,
      canvas:{
        id: 0,
        position:0,
        heigth: 0,
        width: 0,
        type: 'canvas',
        item_list:[{
            id: 13456789,
            position:1,
            heigth: 10,
            width: 6,
            type: 'row',
            item_list:[{
              id: 13456756789,
              position:1,
              heigth: 10,
              width: 6,
              type: 'column',
              item_list:[{
                id: 13456756789,
                position:1,
                heigth: 10,
                width: 6,
                type: 'column',
                item_list:[]
              }]
            }]
        },
        {
            id: 13456789,
            position:1,
            heigth: 10,
            width: 6,
            type: 'row',
            item_list:[{
              id: 13456756789,
              position:1,
              heigth: 10,
              width: 6,
              type: 'column',
              item_list:[{
                id: 13456756789,
                position:1,
                heigth: 10,
                width: 6,
                type: 'column',
                item_list:[]
              }]
            }]
        }]
      }
    }
  },
  
}
</script>
<style lang="scss">
  .toolbar{
    border: 1px solid;
    width: 100%;
  }
  .workflow{
    border: 1px dashed;
    width: 100%;
    min-height: 100vh;
  }

.item{
  border: 1px dashed;
}
.item-active{
  border: 2px dashed rgb(0, 247, 255);
}
</style>