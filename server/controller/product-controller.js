import productData from '../model/productDataModel.js';
import Product from '../model/productSchema.js';


export const getProducts = async (request, response) => {
    try {
        const products = await Product.find({});

        response.json(products);
    }catch (error) {

    }
}

export const getProductById = async (request, response) => {
    try {
        
        const products = await Product.findOne({ '_id': request.params.id });
        console.log(`>>>>>>>>`,products)
        response.json(products);
    }catch (error) {

    }
}
export const getProductsData = async (request, response) => {
    try {
        const products = await productData.find({});

        response.json(products);
    }catch (error) {
        response.json(error).status(500)
    }
}

export const getProductDataById = async (request, response) => {
    try {
        console.log(`>>>>>>>>>`,request.params.id)
        const products = await productData.findOne({ '_id': request.params.id });
        response.json(products);
    }catch (error) {
        response.json(error).status(500)

    }
}