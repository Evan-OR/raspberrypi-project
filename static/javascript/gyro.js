const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, 16 / 9, 0.1, 1000);
const renderer = new THREE.WebGLRenderer();

renderer.setSize(500, 281);
document.getElementById('gyroSection').appendChild(renderer.domElement);

const geometry = new THREE.BoxGeometry(2, 1, 4);
const material = new THREE.MeshPhongMaterial({ color: 0x00ff00 });
const cuboid = new THREE.Mesh(geometry, material);

scene.add(cuboid);

camera.position.z = 5;

const light = new THREE.DirectionalLight(0xffffff, 1);
light.position.set(5, 5, 2).normalize();
scene.add(light);

const ambientLight = new THREE.AmbientLight(0x404040);
scene.add(ambientLight);

cuboid.position.set(0, -1, 0);
camera.lookAt(cuboid.position);

const degreesToRadians = (deg) => (deg * Math.PI) / 180;

const animate = () => {
  requestAnimationFrame(animate);

  const targetQuaternion = new THREE.Quaternion();
  targetQuaternion.setFromEuler(
    new THREE.Euler(
      degreesToRadians(gGyroData.pitch - gGyroCalibratedRotation.pitch),
      degreesToRadians(-(gGyroData.yaw - gGyroCalibratedRotation.yaw)),
      degreesToRadians(-gGyroData.roll - -gGyroCalibratedRotation.roll)
    )
  );

  cuboid.quaternion.slerp(targetQuaternion, 0.1);

  renderer.render(scene, camera);
};

animate();
