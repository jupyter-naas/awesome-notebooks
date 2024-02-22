import mongoose from 'mongoose';
import autoIncrement from 'mongoose-auto-increment';

const productSchema = new mongoose.Schema({
    id: String,
    url: String,
    detailUrl: String,
    title: Object,
    price: Object,
    quantity: Number,
    description: String,
    discount: String,
    tagline: String
});

autoIncrement.initialize(mongoose.connection);
productSchema.plugin(autoIncrement.plugin, 'product');

const products = mongoose.model('product', productSchema);

export default products;