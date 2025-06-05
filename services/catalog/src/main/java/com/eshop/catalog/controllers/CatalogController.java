package com.eshop.catalog.controllers;

import com.eshop.catalog.dto.CatalogItemDTO;
import com.eshop.catalog.services.CatalogService;
import org.springframework.core.io.Resource;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class CatalogController {
    private CatalogService catalogService;
    public CatalogController(CatalogService catalogService){
        this.catalogService = catalogService;
    }

    @GetMapping("/items")
    public List<CatalogItemDTO> GetCatalogItems()
    {
return this.catalogService.getAllItems();
    }

    @GetMapping("/items/by")
    public List<CatalogItemDTO> GetCatalogItemsByIds(@RequestParam List<Integer> ids)
    {
return this.catalogService.getItemsByIds(ids);
    }

    @GetMapping("/items/by/{id}")
    public CatalogItemDTO GetCatalogItemById(@PathVariable Integer id)
    {
return this.catalogService.getItemsById(id);
    }

    @GetMapping("/items/byName/{name}")
    public List<CatalogItemDTO> GetCatalogItemsByName(@PathVariable String name)
    {
        return this.catalogService.getItemsByName(name);
    }

    @GetMapping("/items/{id}/pic")
    public ResponseEntity<Resource> GetCatalogItemPictureById(@PathVariable Integer id)
    {
        System.out.println(id);
      return this.catalogService.getCatalogItemPictureById(id);
    }
}
