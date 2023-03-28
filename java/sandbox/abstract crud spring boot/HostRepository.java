package com.alvonellos.uptime.repo;

import com.alvonellos.uptime.entity.HostEntity;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.UUID;

@Repository
public interface HostRepository extends JpaRepository<HostEntity, UUID> {
}
