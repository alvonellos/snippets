package com.alvonellos.uptime.service;

import com.alvonellos.uptime.dto.HostDto;
import com.alvonellos.uptime.entity.HostEntity;
import com.alvonellos.uptime.repo.AbstractCrudRepo;
import org.springframework.stereotype.Service;

@Service
public class HostService extends AbstractCrudService<HostDto, HostEntity> {
    public HostService(AbstractCrudRepo<HostEntity> repository) {
        super(repository);
    }
}
