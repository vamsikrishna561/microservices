package com.eshop.catalog.mappers;
import com.eshop.catalog.dto.CatalogBrandDTO;
import com.eshop.catalog.dto.CatalogItemDTO;
import com.eshop.catalog.dto.CatalogTypeDTO;
import com.eshop.catalog.entities.CatalogBrand;
import com.eshop.catalog.entities.CatalogItem;
import com.eshop.catalog.entities.CatalogType;
import org.mapstruct.Mapper;
@Mapper(componentModel="spring")
public interface CatalogMapper {

   CatalogItemDTO toDTO(CatalogItem dto);
   CatalogItem toEntity(CatalogItemDTO entity);
   CatalogTypeDTO toDTO(CatalogType item);
    CatalogType toEntity(CatalogTypeDTO item);
    CatalogBrandDTO toDTO(CatalogBrand item);
    CatalogBrand toEntity(CatalogBrandDTO item);
}
