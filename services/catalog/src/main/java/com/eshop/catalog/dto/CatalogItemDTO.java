package com.eshop.catalog.dto;

import com.eshop.catalog.entities.CatalogBrand;
import com.eshop.catalog.entities.CatalogType;

import java.math.BigDecimal;

public class CatalogItemDTO {
    private int id;

    public int getId() {
        return id;
    }

    @Override
    public String toString() {
        return "CatalogItemDTO{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", catalogType=" + catalogType +
                ", catalogBrand=" + catalogBrand +
                ", availableStock=" + availableStock +
                ", onReorder=" + onReorder +
                ", restockThreshold=" + restockThreshold +
                ", maxStockThreshold=" + maxStockThreshold +
                ", description='" + description + '\'' +
                ", price=" + price +
                ", pictureFileName='" + pictureFileName + '\'' +
                '}';
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public CatalogTypeDTO getCatalogType() {
        return catalogType;
    }

    public void setCatalogType(CatalogTypeDTO catalogType) {
        this.catalogType = catalogType;
    }

    public CatalogBrandDTO getCatalogBrand() {
        return catalogBrand;
    }

    public void setCatalogBrand(CatalogBrandDTO catalogBrand) {
        this.catalogBrand = catalogBrand;
    }

    public int getAvailableStock() {
        return availableStock;
    }

    public void setAvailableStock(int availableStock) {
        this.availableStock = availableStock;
    }

    public boolean isOnReorder() {
        return onReorder;
    }

    public void setOnReorder(boolean onReorder) {
        this.onReorder = onReorder;
    }

    public int getRestockThreshold() {
        return restockThreshold;
    }

    public void setRestockThreshold(int restockThreshold) {
        this.restockThreshold = restockThreshold;
    }

    public int getMaxStockThreshold() {
        return maxStockThreshold;
    }

    public void setMaxStockThreshold(int maxStockThreshold) {
        this.maxStockThreshold = maxStockThreshold;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public BigDecimal getPrice() {
        return price;
    }

    public void setPrice(BigDecimal price) {
        this.price = price;
    }

    public String getPictureFileName() {
        return pictureFileName;
    }

    public void setPictureFileName(String pictureFileName) {
        this.pictureFileName = pictureFileName;
    }

    private String name;
    private CatalogTypeDTO catalogType;
    private CatalogBrandDTO catalogBrand;
    private int availableStock;
    private boolean onReorder;
    private int restockThreshold;
    private int maxStockThreshold;
    private String description;
    private BigDecimal price;
    private String pictureFileName;
}
