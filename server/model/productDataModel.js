import mongoose from 'mongoose';

const productDataSchema = new mongoose.Schema({
    url: String,
    detailUrl: String,
    title: Object,
    price: Object,
    quantity: Number,
    description: String,
    discount: String,
    tagline: String
});

const productData = mongoose.model('productData', productDataSchema);

export default productData;