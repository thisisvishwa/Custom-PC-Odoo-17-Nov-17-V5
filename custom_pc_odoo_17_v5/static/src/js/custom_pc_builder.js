odoo.define('custom_pc_odoo_17_v5.custom_pc_builder', function (require) {
    "use strict";

    var core = require('web.core');
    var ajax = require('web.ajax');
    var publicWidget = require('web.public.widget');

    var _t = core._t;
    var qweb = core.qweb;

    publicWidget.registry.customPcBuilder = publicWidget.Widget.extend({
        selector: '#custom_pc_builder',
        xmlDependencies: ['/custom_pc_odoo_17_v5/static/src/xml/custom_pc_builder.xml'],

        start: function () {
            var self = this;
            return this._super.apply(this, arguments).then(function () {
                self._updateBuilderUI();
            });
        },

        _updateBuilderUI: function () {
            var self = this;
            ajax.jsonRpc("/shop/get_components", 'call', {}).then(function (data) {
                self.$el.html(qweb.render('custom_pc_odoo_17_v5.custom_pc_builder', {components: data}));
                self._bindDraggable();
                self._bindDroppable();
            });
        },

        _bindDraggable: function () {
            this.$(".component-item").draggable({
                helper: 'clone',
                zIndex: 100,
                appendTo: 'body',
                start: function () {
                    $('.pc-slot').addClass('highlight');
                },
                stop: function () {
                    $('.pc-slot').removeClass('highlight');
                }
            });
        },

        _bindDroppable: function () {
            var self = this;
            this.$(".pc-slot").droppable({
                accept: ".component-item",
                drop: function (event, ui) {
                    var componentId = ui.helper.data('id');
                    var slotType = $(this).data('type');
                    self._addComponentToSlot(componentId, slotType);
                }
            });
        },

        _addComponentToSlot: function (componentId, slotType) {
            var self = this;
            ajax.jsonRpc("/shop/add_component_to_slot", 'call', {
                component_id: componentId,
                slot_type: slotType
            }).then(function (data) {
                if (data.error) {
                    alert(data.error);
                } else {
                    self._updateBuilderUI();
                }
            });
        },
    });

    return publicWidget.registry.customPcBuilder;
});