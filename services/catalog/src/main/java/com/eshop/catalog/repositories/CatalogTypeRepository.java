package com.eshop.catalog.repositories;

import com.eshop.catalog.entities.CatalogItem;
import com.eshop.catalog.entities.CatalogType;
import org.springframework.data.jpa.repository.JpaRepository;

interface CatalogTypeRepository extends JpaRepository<CatalogType,Integer> {
}
