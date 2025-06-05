package com.eshop.catalog.entities;

import jakarta.persistence.*;

import java.io.Serializable;
import java.math.BigDecimal;

@Entity
@Table(name = "Catalog")
public class CatalogItem implements Serializable {
    public int getId() {
        return id;
    }

    @Override
    public String toString() {
        return "CatalogItem{" +
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

    public CatalogType getCatalogType() {
        return catalogType;
    }

    public void setCatalogType(CatalogType catalogType) {
        this.catalogType = catalogType;
    }

    public CatalogBrand getCatalogBrand() {
        return catalogBrand;
    }

    public void setCatalogBrand(CatalogBrand catalogBrand) {
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

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;
    private String name;
    @ManyToOne
    @JoinColumn(name = "CatalogTypeId")
    private CatalogType catalogType;
    @ManyToOne
    @JoinColumn(name = "CatalogBrandId")
    private CatalogBrand catalogBrand;
    @Column(name = "AvailableStock")
    private int availableStock;
    @Column(name = "OnReorder")
    private boolean onReorder;
    @Column(name = "RestockThreshold")
    private int restockThreshold;
    @Column(name = "MaxStockThreshold")
    private int maxStockThreshold;
    @Column(name = "Description")
    private String description;
    @Column(name = "Price")
    private BigDecimal price;
    private String pictureFileName;
}
;
