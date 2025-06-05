package com.eshop.catalog.repositories;

import com.eshop.catalog.entities.CatalogBrand;
import com.eshop.catalog.entities.CatalogItem;
import org.springframework.data.jpa.repository.JpaRepository;

interface CatalogBrandRepository extends JpaRepository<CatalogBrand,Integer> {
}
