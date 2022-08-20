<template lang="">
        <Item v-if="node.item_list && node.item_list.length" @handle-click="handleClick"   :node="node">
            <node v-for="item in node.item_list" :node="item" @handle-click="handleClick"  ></node>
        </Item>
        <Item v-else @handle-click="handleClick" :node="node">
        </Item>
</template>
<script>
import Item from "@/components/Item.vue"
export default {
    name: "node",
    props: {
        node: Object,
        selected_item: Object,
        // handleClick: Function
    },
    components:{
        Item
    },
    methods: {
        handleClick (node) {
                this.$emit('handle-click', node);
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