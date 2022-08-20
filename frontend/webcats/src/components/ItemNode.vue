<template lang="">
    <div>
        <div 
            v-if="node.item_list && node.item_list.length"
            class="p-1 item" 
            :class="`col-md-${node.width}`"
            @click.stop="handleClick(node)"
            
            > 
            <node v-for="item in node.item_list" :node="item" :handle-click="handleClick"></node>
        </div>
        <div 
            v-else
            class="p-1 item" 
            :class="`col-md-${node.width}`"
            @click.stop="handleClick(node)"
            
            > 
        </div>
    </div>
</template>
<script>
export default {
    name: "node",

    props: {
        node: Object,
        // selected_item: Object
        handleClick: Function
    },
    methods: {
        selectedItemSet(node){
            console.log(node)
            this.selected_item = node
        }
    },
    
}
</script>
<style lang="scss">
.item{
  border: 1px dashed;
}
.item-active{
  border: 2px dashed rgb(0, 247, 255);
}
</style>