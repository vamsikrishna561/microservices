package com.eshop.catalog.repositories;

import com.eshop.catalog.entities.CatalogItem;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface CatalogItemRepository extends JpaRepository<CatalogItem,Integer> {
List<CatalogItem> findByNameContainingIgnoreCase(String name);
    List<CatalogItem> findByIdIn(List<Integer> ids);
}
