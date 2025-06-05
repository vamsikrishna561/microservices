package com.eshop.catalog.services;

import com.eshop.catalog.dto.CatalogItemDTO;
import com.eshop.catalog.entities.CatalogItem;
import com.eshop.catalog.mappers.CatalogMapper;
import com.eshop.catalog.repositories.CatalogItemRepository;
import org.springframework.core.io.Resource;
import org.springframework.core.io.ResourceLoader;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

@Service
public class CatalogService {
    private final CatalogItemRepository repository;
    private final CatalogMapper mapper;
    private final ResourceLoader resourceLoader;
    public CatalogService(CatalogItemRepository repository, CatalogMapper mapper, ResourceLoader resourceLoader) {
        this.repository = repository;
        this.mapper = mapper;
        this.resourceLoader = resourceLoader;
    }
    public List<CatalogItemDTO> getAllItems() {
        System.out.println(repository.findAll());
        var items= repository.findAll().stream().map(mapper::toDTO).collect(Collectors.toList());
        System.out.println(items);
        return items;
    }


    public List<CatalogItemDTO> getItemsByIds(List<Integer> ids) {
        return repository.findByIdIn(ids).stream().map(mapper::toDTO).collect(Collectors.toList());
    }

    public List<CatalogItemDTO> getItemsByName(String name) {
        return repository.findByNameContainingIgnoreCase(name).stream().map(mapper::toDTO).collect(Collectors.toList());
    }

    public CatalogItemDTO getItemsById(Integer id) {
        return mapper.toDTO(repository.findById(id).orElse(null));
    }
    public ResponseEntity<Resource> getCatalogItemPictureById(Integer id)  {

        var item = repository.findById(id);
        System.out.println(item);
        if(item.isEmpty())
            return ResponseEntity.notFound().build();
        String filename = "pics/"+ item.get().getPictureFileName();
System.out.println(filename);
        Resource image = resourceLoader.getResource("classpath:static/" + filename);
        if (!image.exists()) {
            return ResponseEntity.notFound().build();
        }

        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.IMAGE_JPEG);

        return new ResponseEntity<>(image, headers, HttpStatus.OK);
    }

}
